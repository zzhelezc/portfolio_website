const buttons = document.querySelectorAll("[data-carousel-button]")

buttons.forEach(button => {
    button.addEventListener("click", () => {
        const offset = button.dataset.carouselButton === "next" ? 1 : -1
        const slides = button
              .closest("[data-carousel]")
              .querySelector("[data-slides]")
         
        const activeSlide = slides.querySelector("[data-active]")
        let newIndex = [...slides.children].indexOf(activeSlide) + offset
        if (newIndex < 0) newIndex = slides.children.length - 1
        if (newIndex >= slides.children.length) newIndex = 0

        // Restore the first image when nav is clicked
        const navItems = document.querySelectorAll("[id=navItem]")
        navItems.forEach(nav => {
            nav.addEventListener("click", () => {
                slides.children[0].dataset.active = true
                delete activeSlide.dataset.active
            })
        });

        slides.children[newIndex].dataset.active = true
        delete activeSlide.dataset.active
    })
});


document.onkeydown = function(e) {
        e = e || window.event;
        if (e.keyCode == '37') {
            prev_buttons = document.querySelectorAll("[id=prev]")
            prev_buttons.forEach(b => {b.click()})
        } else if (e.keyCode == '39') {
            // right -> show next image
            next_buttons = document.querySelectorAll("[id=next]")
            next_buttons.forEach(b => {b.click()})
        }
}




