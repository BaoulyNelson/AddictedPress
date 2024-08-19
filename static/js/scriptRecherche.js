function toggleSearch() {
    const searchContainer = document.getElementById('searchContainer');
    const searchInput = document.getElementById('searchInput');
    
    if (searchContainer.style.display === 'block') {
        searchContainer.style.display = 'none';
    } else {
        searchContainer.style.display = 'block';
        searchInput.focus();  // Active automatiquement le focus du curseur
    }
}
