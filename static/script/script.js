// Toggle sidebar on mobile
const sidebar = document.querySelector('.sidebar');
const mainContent = document.querySelector('.main-content');

document.querySelector('.sidebar-toggle').addEventListener('click', () => {
    sidebar.classList.toggle('active');
    mainContent.classList.toggle('active');
});