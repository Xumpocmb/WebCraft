document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeToggleBtnMobile = document.getElementById('theme-toggle-mobile');

    const applyTheme = (theme) => {
        document.body.classList.remove('light-mode', 'dark-mode');
        document.body.classList.add(theme + '-mode');
        localStorage.setItem('theme', theme);
        if (themeToggleBtn) themeToggleBtn.textContent = theme === 'dark' ? 'Светлая тема' : 'Темная тема';
        if (themeToggleBtnMobile) themeToggleBtnMobile.textContent = theme === 'dark' ? 'Светлая тема' : 'Темная тема';
    };

    const toggleTheme = () => {
        const currentTheme = document.body.classList.contains('dark-mode') ? 'dark' : 'light';
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        applyTheme(newTheme);
    };

    // Initial theme application
    const initialTheme = localStorage.getItem('theme') || 'dark';
    applyTheme(initialTheme);

    if (themeToggleBtn) {
        themeToggleBtn.addEventListener('click', toggleTheme);
    }

    if (themeToggleBtnMobile) {
        themeToggleBtnMobile.addEventListener('click', toggleTheme);
    }
});
