function toggleTheme() {
    const body = document.body;
    body.classList.toggle('dark-mode');
    const isDarkMode = body.classList.contains('dark-mode');
    localStorage.setItem('dark-mode', isDarkMode);
  
    const icon = document.getElementById('themeIcon');
    icon.textContent = isDarkMode ? 'nights_stay' : 'brightness_7';
  }
  
  const darkMode = localStorage.getItem('dark-mode') === 'true';
  if (darkMode) {
    document.body.classList.add('dark-mode');
    document.getElementById('themeIcon').textContent = 'nights_stay';
  }

  