var swiper = new Swiper('.swiper', {
    lazy: true,
    autoHeight: false,
    // navigation: {
    //     nextEl: '.swiper-button-next',
    //     prevEl: '.swiper-button-prev',
    // },
    pagination: {                       
        el: '.swiper-pagination',
        type: 'bullets',
        dynamicBullets: true,
        clickable: true,
    },
    keyboard: {
        enabled: true,
    },
    loop: true,
    effect: 'fade',
    //fadeEffect: { crossFade: true },
});
