const button = document.querySelector(".fablabnavbar__link__menu");
const fablabnavbar = document.querySelector(".fablabnavbar__links");
const fablabnavbar_icon = document.querySelector(".material-icons");
const fablabnavbar_dropdown_button = document.querySelector(".fablabnavbar__dropdown__button")
const fablabnavbar_dropdown_items = document.querySelector(".fablabnavbar__dropdown__items")

// Gestion du toggle du menu

button.addEventListener("click", () => {
    if (fablabnavbar.style.display === '') {
        fablabnavbar.style.display = "flex";
        // FIXME: L'icone de flèche doit changer au clic
        // button.removeChild(fablabnavbar_icon) 

    }
    else {
        fablabnavbar.style.display = "";
    }

})

// Gestion du toggle des sous-menus

fablabnavbar_dropdown_button.addEventListener("click", () => {
    if(fablabnavbar_dropdown_items.style.display === '') {
        fablabnavbar_dropdown_items.style.display = "block";
    }
    else {
        fablabnavbar_dropdown_items.style.display = '';
    }
})