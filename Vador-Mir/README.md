Backend (résumé)
config/db.py : paramètres de connexion à la BDD centralisés.​

models/user.py : table users (id, email unique, password_hash haché, role, created_at) et fonctions pour créer / chercher / vérifier un utilisateur.​

models/ai_request.py : table ai_requests (id, user_id, question, answer_short, created_at) et fonctions pour enregistrer / lister les requêtes IA.​

routes/auth.py : login, logout, éventuellement inscription, toujours avec mot de passe haché et validation serveur (longueur max, format email, etc.).​

routes/ia.py : endpoint /api/chat pour le chatbot (vérifie la session, appelle l’IA, enregistre en BDD).​

routes/admin.py : endpoints protégés pour lister utilisateurs et requêtes IA, accessibles seulement aux admins.​

routes/contact.py : endpoint /contact recevant le formulaire « Nous contacter », avec contrôles stricts sur la longueur des champs et le format d’email.

server.py : démarre le serveur, branche les routes, gère les erreurs (par exemple renvoyer une page d’erreur accessible).​

Frontend (avec accessibilité et formulaires sûrs)
login.html :

formulaire de connexion avec labels, type="email", required, maxlength raisonnables (par ex. 100 pour l’email, 64 pour le mot de passe) ;

messages d’erreur visibles et lisibles ;

page structurée avec main, titres (h1) et texte alternatif si logo.

index.html :

page d’accueil structurée sémantiquement (header, nav, main, footer) ;

navigation claire : Accueil, Chatbot IA, Admin (si admin), Nous contacter, Déconnexion ;

contenu expliquant la finalité du site et mentionnant que l’accessibilité est prise en compte (bon point pour un défi accessibilité).​

chatbot.html :

champ de saisie avec label explicite ;

bouton accessible au clavier ;

historique des échanges dans une liste structurée ;

limitation de longueur en front (par ex. maxlength="500") et en back pour la question.

admin.html :

tableaux d’administration (<table> avec aption>, <thead>, <th>) pour aider les lecteurs d’écran ;

actions déclenchées par des boutons avec texte clair, pas seulement des icônes.

contact.html :

page « Nous contacter » avec formulaire (nom, email, sujet, message) ;

chaque champ a un label, un maxlength (par ex. nom 50, sujet 100, message 500–1000), et required si nécessaire ;

petit paragraphe expliquant ce que vous faites des données (projet étudiant, conservation limitée).

css/style.css :

responsive via flexbox/grid et media queries ;

accessibilité : contrastes suffisants, taille de police, focus visible, pas de texte important dans des images sans alternative texte ;

éviter les animations agressives (clignotements rapides) pour ne pas gêner certains handicaps.​

js/main.js :

logique commune (déconnexion, éventuels messages ARIA pour signaler des erreurs côté JS) ;

aucune donnée sensible (mot de passe, clé API) stockée en clair dans le front.

js/chatbot.js :

envoie les questions au back (/api/chat), affiche la réponse ;

gère les erreurs réseau avec un message clair pour l’utilisateur.

Contraintes prioritaires à intégrer (résumé “check‑list”)
Sécurité & données

Email = identifiant unique.

Mots de passe : jamais en clair, toujours sous forme de hash ; pas de journaux qui stockent les mots de passe.​

Toutes les entrées (login, chatbot, contact) sont limitées en longueur et vérifiées côté serveur, même si elles sont déjà limitées dans le HTML.

Accessibilité (inspirée des normes WCAG / EAA)

Structure HTML sémantique, labels pour tous les champs de formulaire, navigation clavier possible.​

Contrastes textes/fonds et tailles lisibles ; éviter le texte uniquement dans les images.

Informer clairement de l’état (erreur, succès) avec du texte, pas juste des couleurs (important pour daltoniens).​

Responsive design

Layout qui s’adapte aux mobiles, tablettes et PC grâce à flexbox/grid et media queries ; aucun contenu horizontalement rogné.​

Formulaires sûrs et clairs

maxlength en HTML + validation back correspondante (ex. “20 caractères max” appliqué réellement côté serveur).

Messages d’erreur compréhensibles, sans exposer de détails techniques (pas de stack trace).

Transparence & contact

Onglet « Nous contacter » qui explique ce que deviennent les messages et les données (strictement projet Nuit de l’Info).

Mention (dans contact.html ou le README) que vous cherchez à respecter les bonnes pratiques d’accessibilité et de protection des données, même si vous n’êtes pas dans un cadre légal “production” comme ceux décrits par AccessiWay.
