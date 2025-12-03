from flask import Blueprint, request, jsonify, session
from models.ai_request import create_ai_request

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
    fake_reply = (
        "Réponse de démonstration : pour la vraie IA, nous appellerons l'API externe. "
        f"Votre question était « {user_message[:80]}... »"
    )

    # Enregistrement dans la BDD (version courte de la réponse)
    create_ai_request(
        user_id=session["user_id"],
        question=user_message,
        answer_short=fake_reply[:200],
    )

    return jsonify({"reply": fake_reply}), 200

