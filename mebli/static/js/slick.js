$('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    adaptiveHeight: true,
    asNavFor: '.slider-nav'
});

$('.slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    arrows: false,
    asNavFor: '.slider-for',
    adaptiveHeight: true,
    centerMode: true,
    focusOnSelect: true
});
