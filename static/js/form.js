$('form').on('submit', function(event) {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			macro : macro.checked
		},
		type : 'POST',
		url : '/titty'
	})
	.done(function(data) {
		//alert(data);
		$('#t-body').empty();
		$('#t-body').append(data);
	});
	event.preventDefault();
	$('#th').empty();
	$('#th').append('Skill');
	$('#th2').empty();
	$('#th2').append('Method');
	$('#th3').empty();
	$('#th3').append('Total Hours');
	$('#th4').empty();
	$('#th4').append('Training Hours');
	$('#th5').empty();
	$('#th5').append('Money Hours');
	$('#th6').empty();
	$('#th6').append('Achievable XP/HR');
});//gp-form

$('#click').click(function () {
	$.ajax({
		data : {
			macro : macro.checked,
			level : $('#my-level').val()
		},
		type: 'POST',
		url: '/5m',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			document.getElementById('my-gp').value = '5m';
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//5m

$('#click2').click(function () {
	$.ajax({
		data : {
			macro : macro.checked,
			level : $('#my-level').val()
		},
		type: 'POST',
		url: '/2_5m',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			document.getElementById('my-gp').value = '2.5m';
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//2.5m click

$('#click3').click(function () {
	$.ajax({
		data : {
			macro : macro.checked,
			level : $('#my-level').val()
		},
		type: 'POST',
		url: '/1m',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			document.getElementById('my-gp').value = '1m';
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//1m click

$('#herblore').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Herblore',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//herblore click

$('#prayer').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Prayer',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//prayer click

$('#crafting').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Crafting',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//crafting click

$('#magic').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Magic',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//magic click

$('#fletching').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Fletching',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//fletching click

$('#smithing').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Smithing',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//smithing click

$('#construction').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Construction',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//construction click

$('#firemaking').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Firemaking',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//firemaking click

$('#cooking').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Cooking',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//cooking click

$('#experience').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			macro : macro.checked
		},
		type: 'POST',
		url: '/titty',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//experience click

$('#experience2').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			macro : macro.checked
		},
		type: 'POST',
		url: '/titty',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//experience2 click

$('#info').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Herblore'
		},
		type: 'POST',
		url: '/info',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#th').empty();
			$('#th').append('FAQs');
			$('#th2').empty();
			$('#th3').empty();
			$('#th4').empty();
			$('#th5').empty();
			$('#th6').empty();
			$('#t-body').empty();
			$('#t-body').append(response);

		}
	});
});//info click

$('#btc').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			skill : 'Herblore'
		},
		type: 'POST',
		url: '/btc',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#th').empty();
			$('#th').append('Cryptocurrencies');
			$('#th2').empty();
			$('#th3').empty();
			$('#th4').empty();
			$('#th5').empty();
			$('#th6').empty();
			$('#t-body').empty();
			$('#t-body').append(response);
		}
	});
});//BTC click

$('#herblore2').click(function () {
	$.ajax({
		data : {
			gp : $('#my-gp').val(),//text field into variable
			level : $('#my-level').val(),
			skill : 'Herblore',
			macro : macro.checked
		},
		type: 'POST',
		url: '/lover',//name of the function in the app
		success: function (response) {
			//alert(JSON.stringify(response));//string version of the response
			$('#t-body').empty();
			$('#t-body').append(response);
			$('#th').empty();
			$('#th').append('Skill');
			$('#th2').empty();
			$('#th2').append('Method');
			$('#th3').empty();
			$('#th3').append('Total Hours');
			$('#th4').empty();
			$('#th4').append('Training Hours');
			$('#th5').empty();
			$('#th5').append('Money Hours');
			$('#th6').empty();
			$('#th6').append('Achievable XP/HR');
		}
	});
});//herblore click

