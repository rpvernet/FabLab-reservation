const burgerContainer = document.querySelector(".burger__container");
const nav = document.querySelector(".navbar");

burgerContainer.addEventListener('click', function() {
    this.classList.toggle("open");
    nav.classList.toggle("open-nav");
}) 