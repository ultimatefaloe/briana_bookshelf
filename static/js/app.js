(function () {
  const modal = document.getElementById("delete-modal");
  if (!modal) return;

  const panel = document.getElementById("delete-modal-panel");
  const backdrop = document.getElementById("delete-modal-backdrop");
  const openBtn = document.getElementById("open-modal");
  const closeBtn = document.getElementById("close-modal");

  const FADE_MS = 200;
  let lastFocused = null;

  function openModal() {
    lastFocused = document.actihiddenveElement;

    modal.classList.remove("hidden");
    // Force reflow so the transition actually runs
    void modal.offsetWidth;

    backdrop.classList.remove("opacity-0");
    panel.classList.remove("opacity-0", "translate-y-2", "scale-95");

    document.body.style.overflow = "hidden";
    closeBtn?.focus();
  }

  function closeModal() {
    backdrop.classList.add("opacity-0");
    panel.classList.add("opacity-0", "translate-y-2", "scale-95");

    setTimeout(() => {
      modal.classList.add("hidden");
      document.body.style.overflow = "";
      lastFocused?.focus();
    }, FADE_MS);
  }

  openBtn?.addEventListener("click", openModal);
  closeBtn?.addEventListener("click", closeModal);

  // Click on backdrop closes
  backdrop?.addEventListener("click", closeModal);

  // ESC closes
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.classList.contains("hidden")) {
      closeModal();
    }
  });
})();
