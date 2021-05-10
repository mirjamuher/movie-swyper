// Make genre-cards selectable
function setupPage() {
    for (const elGenre of document.querySelectorAll(".genre-card")) {
        elGenre.addEventListener("click", chooseGenre)
    }
}

function chooseGenre(event) {
    const elGenre = event.currentTarget;
    const elCheckbox = elGenre.querySelector('input[type=checkbox]')

    if (elGenre.classList.contains("selected")) {
        elGenre.classList.remove("selected");
        elCheckbox.checked = false;
    } else {
        elGenre.classList.add("selected");
        elCheckbox.checked = true;
    }
}

document.addEventListener("DOMContentLoaded", setupPage);
