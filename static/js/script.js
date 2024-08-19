
function updateTime() {
    const now = new Date();
    const options = { year: 'numeric', month: 'short', day: 'numeric' };
    document.getElementById('date-time').innerText = now.toLocaleDateString('fr-FR', options);
}

setInterval(updateTime, 1000);
updateTime();
