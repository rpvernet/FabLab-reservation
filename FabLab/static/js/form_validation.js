// FIXME: Tous les clics mènent vers une demande de confirmation

const forms = document.querySelectorAll('.js-form-confirmation')

forms.forEach((form) => {
    const confirmation = confirm('Êtes-vous certain de vouloir supprimer cette réservation ?')
    return form.onsubmit = () => confirmation ? true : false
})