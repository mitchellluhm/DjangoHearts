$(document).ready(function(){

	var turn_number;

	function html_to_string(html){
		// extract just the val and suit from html string
		var start = html.indexOf("/images/");
		var end = html.indexOf(".png");

		// if not neg
		start = start + 8;
		var card_str = html.slice(start, end);
		console.log(card_str);
		return card_str;
	}	

	function val_to_code(c_val){
		var code = "";
		switch(c_val){
			case "ace":
				code = "A";
				break;
			case "king":
				code = "K";
				break;
			case "queen":
				code = "Q";
				break;
			case "jack":
				code = "J";
				break;
			case "10":
				code = "X";
				break;
			case "9":
				code = "9";
				break;
			case "8":
				code = "8";
				break;
			case "7":
				code = "7";
				break;
			case "6":
				code = "6";
				break;
			case "5":
				code = "5";
				break;
			case "4":
				code = "4";
				break;
			case "3":
				code = "3";
				break;
			case "2":
				code = "2";
				break;
			default:
				code = "0";
		}
		return code;
	}

	function suit_to_code(c_suit){
		var code = "";
		switch(c_suit){
			case "clubs":
				code = "C";
				break;
			case "spades":
				code = "S";
				break;
			case "diamonds":
				code = "D";
				break;
			case "hearts":
				code = "H";
				break;
			default:
				code = "0";
		}
		return code;
	}

	function string_to_textcode(card_str){
		// 7_of_diamonds -> 7D
		var of = card_str.indexOf("_of_");
		var c_val = card_str.slice(0, of);
		var c_suit = card_str.slice(of + 4);
		var v_code = val_to_code(c_val);
		var s_code = suit_to_code(c_suit);
		var code = "";
		if (v_code !== "0" && s_code !== "0"){
			// code is ok!
			code = v_code;
			code = code.concat(s_code);
			console.log(code);
		}
		return code;
	}

	$(".user_hand").width($(window).width());

	$('.user_slot').click(function(){
		var card_html = $(this).html();
		var card_code = string_to_textcode(html_to_string(card_html));
		$('#id_card').val(card_code);

		$('#center_bottom').html($(this).children('img'));
		$(this).children('img').remove();
		// trigger the next CPU turn
	});
});
