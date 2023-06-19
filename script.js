// const buttons = document.querySelectorAll("[data-carousel-button]")

// buttons.forEach(button => {
//     button.addEventListener("click", () => {
//         const offset = button.dataset.carouselButton === "next" ? 1 : -1
//         const slides = button
//               .closest("[data-carousel]")
//               .querySelector("[data-slides]")

//         const activeSlide = slides.querySelector("[data-active]")
//         let newIndex = [...slides.children].indexOf(activeSlide) + offset
//         if (newIndex < 0) newIndex = slides.children.length - 1
//         if (newIndex >= slides.children.length) newIndex = 0

//         // // Restore the first image when nav is clicked
//         // const navItems = document.querySelectorAll("[id=navItem]")
//         // navItems.forEach(nav => {
//         //     nav.addEventListener("click", () => {
//         //         slides.children[0].dataset.active = true
//         //         delete activeSlide.dataset.active
//         //     })
//         // });

//         slides.children[newIndex].dataset.active = true

//         delete activeSlide.dataset.active
//     })
// });


// document.onkeydown = function(e) {
//     e = e || window.event;
//     if (e.keyCode == '37') {
//         prev_buttons = document.querySelectorAll("[id=prev]")
//         prev_buttons.forEach(b => {b.click()})
//     } else if (e.keyCode == '39') {
//         // right -> show next image
//         next_buttons = document.querySelectorAll("[id=next]")
//         next_buttons.forEach(b => {b.click()})
//     }
// }


// (function () {
//     function logElementEvent(eventName, element) {
//         console.log(Date.now(), eventName, element.getAttribute("data-src"));
//     }

//     var callback_enter = function (element) {
//         logElementEvent("🔑 ENTERED", element);
//     };
//     var callback_exit = function (element) {
//         logElementEvent("🚪 EXITED", element);
//     };
//     var callback_loading = function (element) {
//         logElementEvent("⌚ LOADING", element);
//     };
//     var callback_loaded = function (element) {
//         logElementEvent("👍 LOADED", element);
//     };
//     var callback_error = function (element) {
//         logElementEvent("💀 ERROR", element);
//         element.src = "https://via.placeholder.com/440x560/?text=Error+Placeholder";
//     };
//     var callback_finish = function () {
//         logElementEvent("✔️ FINISHED", document.documentElement);
//     };
//     var callback_cancel = function (element) {
//         logElementEvent("🔥 CANCEL", element);
//     };

//     var ll = new LazyLoad({
//         class_applied: "lz-applied",
//         class_loading: "lz-loading",
//         class_loaded: "lz-loaded",
//         class_error: "lz-error",
//         class_entered: "lz-entered",
//         class_exited: "lz-exited",
//         // Assign the callbacks defined above
//         callback_enter: callback_enter,
//         callback_exit: callback_exit,
//         callback_cancel: callback_cancel,
//         callback_loading: callback_loading,
//         callback_loaded: callback_loaded,
//         callback_error: callback_error,
//         callback_finish: callback_finish
//     });
// })();

// // $(window).load(function() {
// //     $('.flexslider').flexslider({
// //         animation: "slide",
// //         controlNav: false
// //         // controlsContainer: $(".custom-controls-container"),
// //         // customDirectionNav: $(".custom-navigation a")
// //     });
// // });


// // $(document).on('ready', function() {

// //     $('.slider').slick({
// //         dots: false,
// //         speed: 300,
// //         slidesToShow: 1,
// //         draggable: true,
// //         swipeToSlide: true,
// //         arrows: false,
// //         accessibility: true,
// //     });

// // });



var swiper = new Swiper('.swiper', {
      // Enable lazy loading
    lazy: true,
    autoHeight: false,
    keyboard: {
        enabled: true,
    },
    loop: true,
    effect: 'slide',
    fadeEffect: { crossFade: true },
    history: {
        replaceState: true,
        key: 'image',
    }
});
