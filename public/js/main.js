$(document).ready(function() {
	var logo_url = $('#logo').attr('src');
	var logo_url_hover = logo_url.split('Light')[0]+'.png';
	$('#logo').hover(
		function() {
			$(this).attr('src',logo_url_hover);		
		},
		function() {
			$(this).attr('src',logo_url);
		}
	);
});
