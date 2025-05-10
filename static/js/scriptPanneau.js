        const menuToggle = document.querySelector('.mobile-menu-toggle');
        const closePanelButton = document.querySelector('.close-panel-button');
        const mobileSidePanel = document.getElementById('mobileSidePanel');
        // const body = document.body; // Décommenter si vous utilisez le blocage du scroll

        function openPanel() {
            if (mobileSidePanel) {
                mobileSidePanel.classList.add('active');
            }
            if (menuToggle) {
                menuToggle.setAttribute('aria-expanded', 'true');
            }
            // Optionnel: empêcher le scroll du body quand le panneau est ouvert
            // body.style.overflow = 'hidden';
        }

        function closePanel() {
            if (mobileSidePanel) {
                mobileSidePanel.classList.remove('active');
            }
            if (menuToggle) {
                menuToggle.setAttribute('aria-expanded', 'false');
            }
            // Optionnel: restaurer le scroll du body
            // body.style.overflow = '';
        }

        if (menuToggle) {
            menuToggle.addEventListener('click', () => {
                if (mobileSidePanel && mobileSidePanel.classList.contains('active')) {
                    closePanel();
                } else {
                    openPanel();
                }
            });
        }

        if (closePanelButton) {
            closePanelButton.addEventListener('click', closePanel);
        }
