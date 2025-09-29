// main.js - small UX niceties (optional)
// - reveal-on-scroll helper (add class "reveal-on-scroll" to elements to animate)
// - "/" keyboard shortcut to focus name input

document.addEventListener('DOMContentLoaded', () => {
  // Reveal-on-scroll
  const reveals = document.querySelectorAll('.reveal-on-scroll');
  if ('IntersectionObserver' in window && reveals.length) {
    const obs = new IntersectionObserver((entries, observer) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('opacity-100', 'translate-y-0');
          observer.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });

    reveals.forEach(el => {
      el.classList.add('opacity-0', 'translate-y-6', 'transition-all', 'duration-700');
      obs.observe(el);
    });
  }

  // Shortcut: press "/" to focus contact name
  document.addEventListener('keydown', (ev) => {
    if (ev.key === '/') {
      const name = document.querySelector('input[name="name"]');
      if (name) {
        ev.preventDefault();
        name.focus();
      }
    }
  });
});
