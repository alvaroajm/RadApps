(() => {
  let saved;
  try { saved = localStorage.getItem('radapps-theme'); } catch (_) {}
  const dark = saved === 'dark' || (saved !== 'light' && window.matchMedia('(prefers-color-scheme: dark)').matches);
  document.documentElement.dataset.theme = dark ? 'dark' : 'light';
})();
