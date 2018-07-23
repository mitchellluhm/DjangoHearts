$(document).ready(function(){

	$(".user_hand").width($(window).width());

	$('.user_slot').click(function(){
		// check if this is a valid move
		//
		// move card if valid
		//
		// prompt user to select different card if invalid
		$('#center_bottom').html($(this).children('img'));
		$(this).children('img').remove();
		// trigger the next CPU turn
	});
});
