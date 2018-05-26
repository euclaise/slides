var x = 0;
document.addEventListener("keydown", function(event) {
	console.log(event.keyCode);
	if (event.keyCode === 13) {
		x++;
		$('html, body').animate(
			{ 
				scrollTop: 15+parseInt( $("#break-"+x).offset().top)
			}, 2000);
		}
		return false;
});