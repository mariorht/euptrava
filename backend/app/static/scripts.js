// Redirigir al usuario al backend para autenticarse con Strava
function authenticate() {
    window.location.href = "/auth/login";
}


// Capturar el token de la URL y almacenarlo
window.onload = function () {
    const params = new URLSearchParams(window.location.search);
    const token = params.get("token");

    if (token) {
        // Almacenar el token en localStorage
        localStorage.setItem("access_token", token);

        // Limpiar la URL eliminando el token
        window.history.replaceState({}, document.title, "/");
        alert("Autenticación exitosa. Ahora puedes ver tus actividades.");
    }
};


// Obtener actividades del backend
async function fetchActivities() {
    const token = localStorage.getItem("access_token");

    if (!token) {
        alert("Por favor, inicia sesión primero.");
        return;
    }

    try {
        // Enviar el token como parámetro de consulta
        const response = await fetch(`/api/activities?token=${token}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const activities = await response.json();

        const list = document.getElementById("activities-list");
        list.innerHTML = ""; // Limpiar la lista antes de agregar nuevas actividades

        activities.forEach(activity => {
            const listItem = document.createElement("li");
            listItem.textContent = `${activity.name} - ${activity.distance} metros`;
            list.appendChild(listItem);
        });
    } catch (error) {
        console.error("Error al obtener actividades:", error);
    }
}
