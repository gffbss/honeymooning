$(document).ready(function() {
	$('#message-submit').click(function(){
		subject = $('#subject option:selected').val();
		name = $('#name').val();
		email = $('#email').val();
		message = $("#message").val();
    	console.log('Clicked Fucker!');
    	console.log(name, email, message, subject);
	});
});