// admin.js
// Remplit les tableaux de admin.html à partir des APIs JSON

document.addEventListener("DOMContentLoaded", () => {
    const usersBody = document.getElementById("users-table-body");
    const aiBody = document.getElementById("ai-requests-table-body");

    if (usersBody) {
        loadUsers(usersBody);
    }
    if (aiBody) {
        loadAiRequests(aiBody);
    }
});

function loadUsers(tbody) {
    fetch("/api/admin/users", { credentials: "include" })
        .then((res) => res.json())
        .then((data) => {
            tbody.innerHTML = "";
            if (!Array.isArray(data)) {
                return;
            }
            data.forEach((user) => {
                const tr = document.createElement("tr");

                tr.innerHTML = `
                    <td>${user.email}</td>
                    <td>${user.role}</td>
                    <td>${user.created_at}</td>
                    <td>
                        <!-- Boutons non fonctionnels pour l'instant -->
                        <button type="button" class="btn-small">Rendre user</button>
                        <button type="button" class="btn-small btn-danger">Supprimer</button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        })
        .catch((err) => {
            console.error(err);
        });
}

function loadAiRequests(tbody) {
    fetch("/api/admin/ai-requests", { credentials: "include" })
        .then((res) => res.json())
        .then((data) => {
            tbody.innerHTML = "";
            if (!Array.isArray(data)) {
                return;
            }
            data.forEach((req) => {
                const tr = document.createElement("tr");
                tr.innerHTML = `
                    <td>${req.created_at}</td>
                    <td>${req.user_email}</td>
                    <td>${req.question.slice(0, 60)}...</td>
                    <td>${req.answer_short ? "Succès" : "N/A"}</td>
                `;
                tbody.appendChild(tr);
            });
        })
        .catch((err) => {
            console.error(err);
        });
}
