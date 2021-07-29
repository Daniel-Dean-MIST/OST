$(document).ready(function() {



	$('#prayer').click(function () {
		$.ajax({
			data : {
				gp : $('#my-gp').val(),//text field into variable
				skill : 'Prayer'
			},
			type: 'POST',
			url: '/lover',//name of the function in the app
			success: function (response) {
				//alert(JSON.stringify(response));//string version of the response
				$('#t-body').empty();
				$('#t-body').append(response);
			}
		});
	});//prayer click
});