// ===========================
// main.js
// Script global pour le front
// - gestion du bouton "Déconnexion"
// - helpers pour afficher les erreurs sur les formulaires
// ===========================

// Cette fonction est appelée quand la page est chargée
document.addEventListener("DOMContentLoaded", () => {
    // Récupère le bouton de déconnexion s’il existe sur la page
    const logoutBtn = document.getElementById("logout-btn");

    // Si le bouton est présent (pages index, chatbot, admin, contact),
    // on lui ajoute un gestionnaire de clic
    if (logoutBtn) {
        logoutBtn.addEventListener("click", handleLogout);
    }
});

// ---------------------------
// Déconnexion
// ---------------------------

/**
 * Gère la déconnexion de l'utilisateur.
 * L'idée :
 *  - appeler le backend sur /logout (si tu l’implémentes),
 *  - nettoyer éventuellement un token local,
 *  - rediriger vers la page de login.
 */
function handleLogout() {
    // Exemple : appel fetch vers /logout (tu pourras adapter selon ton back)
    fetch("/logout", {
        method: "GET",
        credentials: "include" // envoie les cookies de session si besoin
    }).finally(() => {
        // Quoi qu'il arrive (succès ou erreur), on renvoie l'utilisateur vers login.html
        window.location.href = "login.html";
    });
}

// ---------------------------
// Helpers pour afficher une erreur dans un élément <p> dédié
// ---------------------------

/**
 * Affiche un message d’erreur dans un élément ayant l’ID donné.
 * @param {string} elementId - ID de l’élément (par ex. "login-error").
 * @param {string} message - Texte de l’erreur à afficher.
 */
function showError(elementId, message) {
    const el = document.getElementById(elementId);
    if (el) {
        el.textContent = message;
    }
}

/**
 * Efface le message d’erreur dans l’élément ciblé.
 * @param {string} elementId - ID de l’élément.
 */
function clearError(elementId) {
    const el = document.getElementById(elementId);
    if (el) {
        el.textContent = "";
    }
}

// On exporte les fonctions dans l’espace global pour les réutiliser dans d’autres scripts
window.appHelpers = {
    showError,
    clearError
};
