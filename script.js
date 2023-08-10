var swiper = new Swiper('.swiper', {
    lazy: true,
    autoHeight: false,
    keyboard: {
        enabled: true,
    },
    pagination: {                       
        el: '.swiper-pagination',
        type: 'bullets',
        dynamicBullets: true,
        clickable: true,
    },
    loop: true,
    effect: 'slide',
    // fadeEffect: { crossFade: true },
});
