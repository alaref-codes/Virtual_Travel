$(function () {
    
    $('.invisible img').on('click', function () {
        $(this).siblings().removeClass('selected');
        $(this).addClass('selected');
        $('.main-img img').hide().attr('src', $(this).attr('src')).fadeIn(500);
    });
    $('.fa-chevron-right').on('click', function () {
        if ($('.invisible img.selected').is(':last-child')) {

            $('.invisible img').eq(0).click()
        } else {
            $('.invisible img.selected').next().click();
        }
    });
    function change() {
        $('.fa-chevron-right').click();
    }
    setInterval(change, 3000);

    //for country height

    $('.country').css({
        height: $('.country').innerHeight() + 30
    });

    //this for chevron click
    $('#chevron i').on('click', function () {

        if ($(window).scrollTop() < $(this).offset().top-50) {
            $('body , html').animate({
                scrollTop: $('.title-text .container h2').offset().top
            }, 200);
            $(this).css({
                'transform':'rotate('+180+'deg)',
            });
        }else{
            $('body , html').animate({
                scrollTop: 0
            }, 200);
            $(this).css({
                'transform':'rotate('+360+'deg)',
            });
            
        }
    });

    //this for chevron scroll
    $(window).on('scroll',function(){
        chev=$('#chevron i')
        if($(this).scrollTop() > chev.offset().top-50){

            $(chev).css({
                'transform':'rotate('+180+'deg)',
            });
        }else{

            $(chev).css({
                'transform':'rotate('+360+'deg)',
            });
        }

    });
    //countries page code

    //scroll to element code

    $('li').on('click', function () {
        $('body , html').stop()
        $('body , html').animate({
            scrollTop: $($(this).attr('data-scroll')).offset().top
        }, 500);

    });

    $('.sec-nav .search form input').val('serch by country name').css('color','#8a8282');
    $('.sec-nav .search form input').on('focus',function(){
        $(this).val('').css('color','#000');
    });
    $('.sec-nav .search form input').on('blur',function(){
        if($(this).val()===''){
            $(this).val('serch by country name').css('color','#8a8282');               
        }
    });
    $('.sec-nav .search form').on('submit',function(e){
        if($('.sec-nav .search form input').val()==='serch by country name'){
            e.preventDefault();
        }

    }); 
});