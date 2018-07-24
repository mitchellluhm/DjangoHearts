$(document).ready(function(){

	var turn_number;

	function check_valid_move() {
		// takes a card user wants to play, see if they can play it
	}	

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
