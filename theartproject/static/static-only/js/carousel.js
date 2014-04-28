// JavaScript Document

$(document).ready(function() {
	
	var leftPos = 0;
	
	$("#btnRight").click(function(){
		
		console.log(leftPos);
		
		if(leftPos % 960 === 0 && leftPos >= 0 && leftPos <= 1920){
			$("#slideshow_ul").animate({
				left: '-=960'
			}, 300);
			leftPos += 960;
			}
	});
	
	$("#btnLeft").click(function(){
		
		if(leftPos % 960 === 0 && leftPos <=3840 && leftPos >= 960){
			$("#slideshow_ul").animate({
				left: '+=960'
			}, 300);
			leftPos -= 960;
			}
		
		});
});