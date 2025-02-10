document.addEventListener("DOMContentLoaded", function () {
    const searchContainer = document.getElementById("searchContainer");
    const searchInput = document.getElementById("searchInput");

    function toggleSearch() {
        if (searchContainer.style.display === "none" || searchContainer.style.display === "") {
            searchContainer.style.display = "block";
            searchInput.focus(); // Met le curseur dans le champ
        } else {
            searchContainer.style.display = "none";
        }
    }

    // Fermer si on clique en dehors
    document.addEventListener("click", function (event) {
        if (!searchContainer.contains(event.target) && !event.target.closest(".search-icon")) {
            searchContainer.style.display = "none";
        }
    });

    // Ajoute l'événement au clic sur l'icône
    document.querySelector(".search-icon").addEventListener("click", toggleSearch);
});
