(() => {
  const root = document.documentElement;
  const en = root.lang === 'en';
  const theme = document.querySelector('.theme-toggle');
  const media = window.matchMedia('(prefers-color-scheme: dark)');
  const labelTheme = () => {
    const dark = root.dataset.theme === 'dark';
    theme.setAttribute('aria-label', en ? `Switch to ${dark ? 'light' : 'dark'} mode` : `Mudar para o modo ${dark ? 'claro' : 'escuro'}`);
    theme.setAttribute('aria-pressed', String(dark));
  };
  labelTheme();
  theme.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    try { localStorage.setItem('radapps-theme', root.dataset.theme); } catch (_) {}
    labelTheme();
  });
  media.addEventListener('change', event => {
    let saved;
    try { saved = localStorage.getItem('radapps-theme'); } catch (_) {}
    if (!saved) { root.dataset.theme = event.matches ? 'dark' : 'light'; labelTheme(); }
  });
  const toggle = document.querySelector('.menu-toggle');
  const menu = document.querySelector('.nav-links');
  const setMenu = open => { menu.classList.toggle('open', open); toggle.setAttribute('aria-expanded', String(open)); };
  toggle.addEventListener('click', () => setMenu(!menu.classList.contains('open')));
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menu.classList.contains('open')) { setMenu(false); toggle.focus(); }
  });
  document.addEventListener('click', event => {
    if (!event.target.closest('.navbar')) setMenu(false);
  });
  window.matchMedia('(min-width: 801px)').addEventListener('change', event => { if (event.matches) setMenu(false); });
  const syncLanguageLinks = () => document.querySelectorAll('.language-switch a').forEach(link => {
    const target = new URL(link.href);
    target.hash = location.hash;
    link.href = target.href;
  });
  syncLanguageLinks();
  window.addEventListener('hashchange', syncLanguageLinks);
  const reset = document.getElementById('reset-preferences');
  if (reset) reset.addEventListener('click', () => {
    try { localStorage.removeItem('radapps-theme'); } catch (_) {}
    root.dataset.theme = media.matches ? 'dark' : 'light';
    labelTheme();
    document.getElementById('reset-status').textContent = en ? 'Preference cleared. The theme now follows your device.' : 'Preferência removida. O tema agora acompanha seu dispositivo.';
  });
})();
