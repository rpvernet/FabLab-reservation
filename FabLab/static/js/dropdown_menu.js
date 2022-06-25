
const dropdown = document.querySelectorAll(".navbar__dropdown")
const dropdownlvl2 = document.querySelectorAll(".navbar__dropdown__lvl2")
const container = document.querySelector(".container")

const fablabnavbarLinks = document.querySelectorAll(".fablabnavbar__link")


dropdown.forEach((dropdownBloc) => {
    dropdownBloc.addEventListener("click", (e) => {
            let dropdownMenu = dropdownBloc.childNodes[3]
        console.log(dropdownMenu)
            if (dropdownMenu.style.display === '') {
                dropdownMenu.style.display = "block" 
            } 
            
            else {
                dropdownMenu.style.display = ''
            } 
    })
})

dropdownlvl2.forEach((dropdownBloc) => {
    dropdownBloc.addEventListener("click", (e) => {
            let dropdownMenu = dropdownBloc.childNodes[3]
        console.log(dropdownMenu)
            if (dropdownMenu.style.display === '') {
                dropdownMenu.style.display = "block"
            }

            else {
                dropdownMenu.style.display = ''
            }
    })
})

// L'intégration du menu du Fab Lab dans l'événement est pour éviter de dupliquer un eventlistener sur le document

document.addEventListener("click", (e) => {
    dropdown.forEach((dropdownBloc) => {

        // vars pour clics en dehors du menu général
        const dropdownMenu = dropdownBloc.childNodes[3]
        const button = dropdownBloc.childNodes[1]

        if(e.target !== button) {
            dropdownMenu.style.display = ''
        }
        /* Clics en dehors du dropdown dans le menu du Fab Lab
        const fablabnavbarDropdownItems = document.querySelector(".fablabnavbar__dropdown__items")
        const fablabnavbarDropdownButton = document.querySelector(".fablabnavbar__dropdown__button")

        if(e.target !== fablabnavbarDropdownButton) {
            fablabnavbarDropdownItems.style.display = ''
        }
   */
    })
})