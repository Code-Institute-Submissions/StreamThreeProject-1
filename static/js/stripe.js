$(function() {
	
	// function to handle the form submission on the payment form.
	$("#quotePayment").submit(function() {
		// variables to hold the form and card details
		var form = this;
		var card = {
			number:   $("#id_credit_card_number").val(),
			expMonth: $("#id_expiry_month").val(),
			expYear:  $("#id_expiry_year").val(),
			cvc:      $("#id_cvv").val()
		};

		// disable the validate button
		$("#validateCardButton").attr("disabled", true);
		
		// create a Stripe Token and validate the card.
		Stripe.createToken(card, function(status, response) {
			// if the card is valid
			if (status === 200) {
				// log the response in the console.
				//console.log(status, response);

				// hide the error messages.
				$("#credit-card-errors").hide();

				// set the Stripe Token to the hidden Payment ID field.
				$("#id_payment_id").val(response.id);

				// submit the form.
				form.submit();

			} else {
				// set the error message.
				$("#stripe-error-message").text(response.error.message);

				// show the error messages.
				$("#credit-card-errors").show();

				// enable the validate button
				$("#validateCardButton").attr("disabled", false);
			}
		});

		// return false as default.
		return false;
	});
});