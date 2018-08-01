// (function($){
//   $(function(){
//
//     $('.sidenav').sidenav();
//     $('.parallax').parallax();
//     $('select').material_select();
//      $('.dropdown-trigger').dropdown();
//
//   }); // end of document ready
// })(jQuery); // end of jQuery name space
(function($){
  $(function(){
    $('.dropdown-trigger').dropdown();
    $('.fixed-action-btn').floatingActionButton();
    $('.select').formSelect();
    $('.sidenav').sidenav();
    $('.parallax').parallax();
    $('.modal').modal();
    $('.slider').slider();
    $('.tooltipped').tooltip();
    $('html, body').animate({
      scrollTop: $(".intro").offset().top
    }, 2000);


// $('.select').material_select();
  }); // end of document ready
})(jQuery); // end of jQuery name space

var header = $('header');
var range = 200;

$(window).on('scroll', function () {

  var scrollTop = $(this).scrollTop(),
      height = header.outerHeight(),
      offset = height / 1.1,
      calc = 1 - (scrollTop - offset + range) / range;

  header.css({ 'opacity': calc });

  if (calc > '1') {
    header.css({ 'opacity': 1 });
  } else if ( calc < '0' ) {
    header.css({ 'opacity': 0 });
  }

});

$(window).on("load",function() {
  $(window).scroll(function() {
    var windowBottom = $(this).scrollTop() + $(this).innerHeight();
    $(".fade").each(function() {
      /* Check the location of each desired element */
      var objectBottom = $(this).offset().top + $(this).outerHeight();

      /* If the element is completely within bounds of the window, fade it in */
      if (objectBottom < windowBottom) { //object comes into view (scrolling down)
        if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
      } else { //object goes out of view (scrolling up)
        if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
      }
    });
  }).scroll(); //invoke scroll-handler on page-load
});
