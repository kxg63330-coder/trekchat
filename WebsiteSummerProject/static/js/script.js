function toggleMenu() {
    const menu = document.getElementById("nav-menu");
    menu.classList.toggle("open");
}

document.addEventListener("DOMContentLoaded", () => {

    /* ------------------------------
       ROUTE SLIDER (already working)
    ------------------------------ */
    const track = document.querySelector(".slider-track");
    const slides = document.querySelectorAll(".slide");

if (track && slides.length > 0) {
    let index = 0;

    function autoSlide() {
        if (!slides[0]) return;  // ⭐ prevents crash

        index++;
        if (index >= slides.length) index = 0;

        const slideWidth = slides[0].offsetWidth + 20;
        track.style.transform = `translateX(-${index * slideWidth}px)`;
    }

    setInterval(autoSlide, 4000);
}

    /* ------------------------------
       BLOG SLIDER (new)
    ------------------------------ */
    const blogTrack = document.querySelector(".blog-track");
    const blogCards = document.querySelectorAll(".blog-card");

    if (blogTrack && blogCards.length > 0) {
        let blogIndex = 0;

        function autoBlogSlide() {
            blogIndex++;
            if (blogIndex >= blogCards.length) blogIndex = 0;

            if (!blogCards[0]) return;
const cardWidth = blogCards[0].offsetWidth + 20;

            blogTrack.style.transform = `translateX(-${blogIndex * cardWidth}px)`;
        }

        setInterval(autoBlogSlide, 4000);
    }

});
/* ------------------------------
   ROUTE SLIDER (4-card slider)
------------------------------ */
const routeTrack = document.querySelector(".route-track");
const routeSlides = document.querySelectorAll(".route-slide");

if (routeTrack && routeSlides.length > 0) {
    let rIndex = 0;

    function autoRouteSlide() {
        rIndex++;
        if (rIndex >= routeSlides.length) rIndex = 0;

        const slideWidth = routeSlides[0].offsetWidth + 15;
        routeTrack.style.transform = `translateX(-${rIndex * slideWidth}px)`;
    }

    setInterval(autoRouteSlide, 3500);
}
