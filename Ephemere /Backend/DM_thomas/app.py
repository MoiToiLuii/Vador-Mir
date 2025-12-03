from flask import Flask
import requests
import os

app = Flask(__name__)

# Récupère la clé API depuis une variable d'environnement
API_KEY = "V1eiio4A7nyh9Kp66WOC4DSfax2ickL7"
API_URL = "https://api.mistral.ai/v1/chat/completions"

@app.route("/")
def starwars_bio():
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "model": "mistral-tiny",
        "messages": [
            {"role": "system", "content": "Tu es un expert de Star Wars. Tu rendras ta réponses sans donner de commentaire."},
            {"role": "user", "content": "Choisis un personnage de Star Wars au hasard et écris une biographie dans un maximum de 300 mots en Français. "}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=data)
    result = response.json()

    # Récupère le texte généré par l'IA
    bio = result["choices"][0]["message"]["content"]

    # Retourne une page HTML minimaliste
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <title>Biographie Star Wars</title>
    </head>
    <body>
        <h1>Biographie générée par IA</h1>
        <p>{bio}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Démarre le serveur Flask
    app.run(debug=True)
