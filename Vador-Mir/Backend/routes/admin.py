# routes/admin.py
# Routes d'administration (lecture seule pour l'instant)

from flask import Blueprint, jsonify, session
from models.user import list_users
from models.ai_request import list_ai_requests

admin_bp = Blueprint("admin", __name__)


def _ensure_admin():
    """
    Vérifie que l'utilisateur connecté est admin.
    Retourne True si oui, False sinon.
    """
    return session.get("user_role") == "admin"


@admin_bp.route("/api/admin/users", methods=["GET"])
def api_users():
    """
    API JSON pour récupérer la liste des utilisateurs.
    Sera appelée depuis admin.html via JS (plus tard).
    """
    if not _ensure_admin():
        return jsonify({"error": "Non autorisé"}), 401

    rows = list_users(limit=100)
    data = [
        {
            "id": r["id"],
            "email": r["email"],
            "role": r["role"],
            "created_at": r["created_at"],
        }
        for r in rows
    ]
    return jsonify(data), 200


@admin_bp.route("/api/admin/ai-requests", methods=["GET"])
def api_ai_requests():
    """
    API JSON pour récupérer les dernières requêtes IA.
    """
    if not _ensure_admin():
        return jsonify({"error": "Non autorisé"}), 401

    rows = list_ai_requests(limit=50)
    data = [
        {
            "id": r["id"],
            "question": r["question"],
            "answer_short": r["answer_short"],
            "created_at": r["created_at"],
            "user_email": r["user_email"],
        }
        for r in rows
    ]
    return jsonify(data), 200

