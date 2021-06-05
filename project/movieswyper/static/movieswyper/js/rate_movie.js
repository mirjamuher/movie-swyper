function setupPage() {
    const ratingBtns = document.querySelectorAll(".imgBtn")

    for (let btn of ratingBtns) {
        btn.addEventListener("click", rateMovie);
    }
}

async function rateMovie(event) {
    const movieId = event.currentTarget.getAttribute("data-movie-id");
    const rating = parseInt(event.currentTarget.getAttribute("data-rating"), 10);

    const data = { 
        "rating" : rating,
    };

    const response = await fetch(`/api/user/movie/${movieId}/rate`, {
        // calls API player_chooses_card()
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json',
        },
        body: JSON.stringify(data),
    });

    // Style background according to button that was clicked 
    const crntCard = document.querySelector(`[data-card-movie-id="${movieId}"]`);

    crntCard.classList.remove('rating-0', 'rating-1', 'rating-2',  'rating-3');
    crntCard.classList.add(`rating-${rating}`)
}

document.addEventListener("DOMContentLoaded", setupPage);
