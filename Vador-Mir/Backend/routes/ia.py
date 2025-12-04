from flask import Blueprint, request, jsonify, session
from models.ai_request import create_ai_request
import requests
import os

ia_bp = Blueprint("ia", __name__)


@ia_bp.route("/api/chat", methods=["POST"])
def chat():
    if "user_id" not in session:
        return jsonify({"error": "Non autorisé"}), 401

    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()

    if not user_message:
        return jsonify({"error": "Message vide"}), 400

    if len(user_message) > 500:
        return jsonify({"error": "Message trop long"}), 400

    # 1) Récupérer la clé API depuis une variable d'environnement
    api_key = os.environ.get("nmzGQvRcANBzY7UclOkgAXeYO4TAIbpb")
    if not api_key:
        return jsonify({"error": "Clé API manquante côté serveur"}), 500

    api_url = "https://api.mistral.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": "mistral-tiny",
        "messages": [
            {
                "role": "system",
                "content": "Tu es un assistant utile et concis.",
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
    }

    try:
        resp = requests.post(api_url, headers=headers, json=payload, timeout=15)
        resp.raise_for_status()
        result = resp.json()
    except requests.exceptions.RequestException:
        return jsonify({"error": "Erreur lors de l'appel à l'API d'IA"}), 502
    except ValueError:
        return jsonify({"error": "Réponse IA invalide"}), 502

    # Vérifier la structure de la réponse
    choices = result.get("choices") or []
    if not choices or "message" not in choices[0] or "content" not in choices[0]["message"]:
        return jsonify({"error": "Réponse IA incomplète"}), 502

    reply_text = choices[0]["message"]["content"]

    # Enregistrement dans la BDD
    create_ai_request(
        user_id=session["user_id"],
        question=user_message,
        answer_short=reply_text[:200],
    )

    return jsonify({"reply": reply_text}), 200
