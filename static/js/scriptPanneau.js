document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll('.main-nav a');
    const sidebar = document.getElementById('sidebar');

    navLinks.forEach(function(link) {
        const clone = link.cloneNode(true);
        sidebar.appendChild(clone);
    });
});

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    if (sidebar.style.width === '50%') {
        sidebar.style.width = '0';
    } else {
        sidebar.style.width = '50%';
    }
}
