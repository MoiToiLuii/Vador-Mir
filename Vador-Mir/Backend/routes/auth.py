# routes/auth.py
# Routes d'authentification (login / logout)

from flask import Blueprint, request, redirect, url_for, session, flash
from models.user import verify_user_credentials

# Création d'un "Blueprint" Flask pour regrouper les routes d'auth
auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    """
    Traite le formulaire de connexion envoyé depuis login.html.
    - Lit email + password.
    - Vérifie contre la BDD.
    - Si OK : stocke infos dans la session, redirige vers index.html.
    - Sinon : enregistre un message d'erreur et redirige vers login.html.
    """
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "")

    # Vérifications de base côté serveur (toujours, même si déjà faites côté front)
    if not email or not password:
        flash("Veuillez renseigner votre e-mail et votre mot de passe.", "error")
        return redirect("/login.html")

    user = verify_user_credentials(email, password)
    if not user:
        flash("Identifiants invalides.", "error")
        return redirect("/login.html")

    # Authentification réussie : on stocke quelques infos dans la session
    session["user_id"] = user["id"]
    session["user_email"] = user["email"]
    session["user_role"] = user["role"]

    # Redirection vers la page d'accueil front
    return redirect("/index.html")


@auth_bp.route("/logout", methods=["GET"])
def logout():
    """
    Déconnecte l'utilisateur.
    - Efface les infos de session.
    - Redirige vers la page de connexion.
    """
    session.clear()
    return redirect("/login.html")
