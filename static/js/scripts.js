const menuButton = document.getElementById('menu-btn');
const menuItems = document.getElementById('menu-items');
menuButton.addEventListener('click', () => {
  menuItems.classList.toggle('hidden');
  menuItems.classList.toggle('flex');
});
