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

    # Réponse factice (tu brancheras une vraie API plus tard)

    # Récupère la clé API depuis une variable d'environnement
    API_KEY = "nmzGQvRcANBzY7UclOkgAXeYO4TAIbpb"
    API_URL = "https://api.mistral.ai/v1/chat/completions"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": "Répond de manière concise, en mode anarchiste"},
            {"role": "user", "content": ""+user_message+""}
        ]
    }
    response = requests.post(API_URL, headers=headers, json=data)
    result = response.json()

    # Récupère le texte généré par l'IA
    bio = result["choices"][0]["message"]["content"]

    # Enregistrement dans la BDD (version courte de la réponse)
    create_ai_request(
        user_id=session["user_id"],
        question=user_message,
        answer_short=bio[:200],
    )

    return jsonify({"reply": bio}), 200

