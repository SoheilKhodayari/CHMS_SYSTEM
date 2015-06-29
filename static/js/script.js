// Animations
var heartBeat = function(){
		$('div.logo img').animate({"width": "+=15px","height" : "+=15px"},1000);
		$('div.logo img').animate({"width": "-=15px","height" : "-=15px"},1000,heartBeat);
	};
var heartAttack = function(){
		$('div.logo img').animate({"width": "+=30px","height" : "+=30px"},100);
		$('div.logo img').animate({"width": "-=30px","height" : "-=30px"},100,heartAttack);
	};

var dingDong = function(e){
		e.animate({"width": "+=30px"},300);
		e.delay(100).animate({"width": "-=30px"},100);
	};
var round = function(e){
		e.animate({"border-radius": "+=30px"},300);
		e.delay(100).animate({"border-radius": "-=30px"},100);
	};
