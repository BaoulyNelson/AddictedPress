document.addEventListener('DOMContentLoaded', () => {
  const searchContainer = document.getElementById('searchContainer');
  const searchInput = document.getElementById('searchInput');

  const toggleSearchContainer = () => {
    searchContainer.classList.toggle('active');
    if (searchContainer.classList.contains('active')) {
      searchInput.focus();
    }
  };

  const largeSearchButton = document.querySelector('.search-icon-large');
  const smallSearchButton = document.querySelector('.panel-search button');

  if (largeSearchButton) {
    largeSearchButton.addEventListener('click', (e) => {
      e.preventDefault();
      toggleSearchContainer();
    });
  }

  if (smallSearchButton) {
    smallSearchButton.addEventListener('click', (e) => {
      e.preventDefault();
      toggleSearchContainer();
    });
  }
});


 document.addEventListener('DOMContentLoaded', () => {
    const offcanvasEl = document.getElementById('offcanvasRight');
    const searchInput = document.getElementById('searchInput');

    offcanvasEl.addEventListener('shown.bs.offcanvas', () => {
      searchInput.focus();
    });
  });