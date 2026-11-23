const menuToggle = document.querySelector("#menuToggle");
const mainNav = document.querySelector("#mainNav");

menuToggle?.addEventListener("click", () => {
  const isOpen = mainNav.classList.toggle("open");
  menuToggle.setAttribute("aria-expanded", String(isOpen));
  menuToggle.setAttribute("aria-label", isOpen ? "Fechar menu" : "Abrir menu");
});

mainNav?.querySelectorAll("a").forEach((link) => {
  link.addEventListener("click", () => {
    mainNav.classList.remove("open");
    menuToggle?.setAttribute("aria-expanded", "false");
  });
});

let bagCount = 0;
const bagCounter = document.querySelector(".bag-count");
const toast = document.querySelector("#toast");
let toastTimeout;

document.querySelectorAll(".quick-add").forEach((button) => {
  button.addEventListener("click", (event) => {
    event.preventDefault();
    event.stopPropagation();
    bagCount += 1;
    if (bagCounter) bagCounter.textContent = String(bagCount);
    showToast(`${button.dataset.product} foi adicionado à sacola.`);
  });
});

function showToast(message) {
  if (!toast) return;
  toast.textContent = message;
  toast.classList.add("show");
  window.clearTimeout(toastTimeout);
  toastTimeout = window.setTimeout(() => toast.classList.remove("show"), 2600);
}

document.querySelector("#newsletterForm")?.addEventListener("submit", (event) => {
  event.preventDefault();
  const email = document.querySelector("#email");
  const message = document.querySelector("#newsletterMessage");
  if (!email?.checkValidity()) {
    email?.reportValidity();
    return;
  }
  if (message) message.textContent = "Cadastro demonstrativo recebido. A integração de e-mail será configurada futuramente.";
  event.currentTarget.reset();
});


const sortProducts = document.querySelector("#sortProducts");
const categoryGrid = document.querySelector("#categoryGrid");

sortProducts?.addEventListener("change", () => {
  if (!categoryGrid) return;
  const cards = [...categoryGrid.querySelectorAll(".product-card")];
  if (sortProducts.value === "name") {
    cards.sort((a, b) => (a.dataset.name || "").localeCompare(b.dataset.name || "", "pt-BR"));
  }
  cards.forEach((card) => categoryGrid.appendChild(card));
});