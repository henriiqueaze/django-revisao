document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('a[data-confirm]').forEach(function (el) {
    el.addEventListener('click', function (ev) {
      const msg = el.getAttribute('data-confirm') || 'Tem certeza?';
      if (!confirm(msg)) {
        ev.preventDefault();
      }
    });
  });

  const firstInput = document.querySelector('form input, form select, form textarea');
  if (firstInput) firstInput.focus();
});
