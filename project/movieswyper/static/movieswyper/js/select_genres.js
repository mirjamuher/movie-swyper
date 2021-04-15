// Make genre-cards selectable
function setupPage() {
    for (const elGenre of document.querySelectorAll(".genre-card")) {
        elGenre.addEventListener("click", chooseGenre)
    }
}

function chooseGenre(event) {
    const elGenre = event.currentTarget;

    if (elGenre.classList.contains("selected")) {
        elGenre.classList.remove("selected");
    } else {
        elGenre.classList.add("selected");
    }
}

document.addEventListener("DOMContentLoaded", setupPage);
