function testWebP(callback) {

    var webP = new Image();
    webP.onload = webP.onerror = function () {
        callback(webP.height == 2);
    };
    webP.src = "data:image/webp;base64,UklGRjoAAABXRUJQVlA4IC4AAACyAgCdASoCAAIALmk0mk0iIiIiIgBoSygABc6WWgAA/veff/0PP8bA//LwYAAA";
}

testWebP(function (support) {

    if (support == true) {
        document.querySelector('body').classList.add('webp');
    }
});

$(document).ready(function () {

    // Slider
    $('.slider-for').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.slider',
    });
    $('.slider').slick({
        lazyLoad: 'ondemand',
        arrows: true,
        dots: true,
        adaptiveHeight: true,
        slidesToShow: 3,
        speed: 500,
        autoplay: false,
        autoplaySpeed: 4000,
        waitForAnimate: true,
        centerMode: true,
        variableWidth: true,
        asNavFor: '.slider-for',
        focusOnSelect: true,
    });

    // Modal window
    $('.js-open-modal').click(function (event) {
        event.preventDefault();

        var modalName = $(this).attr('data-modal');
        var modal = $('.js-modal[data-modal="' + modalName + '"]');

        modal.addClass('is-show');
        $('.js-modal-overlay').addClass('is-show')
    });

    $('.js-modal-close').click(function () {
        $(this).parent('.js-modal').removeClass('is-show');
        $('.js-modal-overlay').removeClass('is-show');
    });

    $('.js-modal-overlay').click(function () {
        $('.js-modal.is-show').removeClass('is-show');
        $(this).removeClass('is-show');
    })

    // Sticky
    const navOffset = $('.header__nav').offset().top
    $(window).scroll(function () {

        const scrolled = $(this).scrollTop()
        const windowScreen = window.screen.width

        if (windowScreen > 992) {
            if (scrolled > navOffset) {
                $('.header__nav').addClass('header__nav-fixed')
                $('.main-screen').addClass('main-screen--mt')
                $('.gallery').addClass('gallery--mt')

            } else if (scrolled < navOffset) {
                $('.header__nav').removeClass('header__nav-fixed')
                $('.main-screen').removeClass('main-screen--mt')
                $('.gallery').removeClass('gallery--mt')
                console.log("Hello")
            }
        }
    })

    // Spoiler
    $('.footer-title').click(function (event) {
        $(this).toggleClass('active').next().slideToggle(300)
    })

    // Burger
    $(".header__menu-toggle").click(function () {
        $(this).toggleClass("active");
        $('.header__menu').slideToggle(300, function () {
            if ($(this).css('display') === "none") {
                $(this).removeAttr('style');
            }
        });
    });
})

