/*!
 * This function builds the help guide to help people navigate around the site.
 */
function beginSiteHelp(stepNumber) {

	// declare the variable to hold the intro.
	var siteHelp = introJs();
	var url = window.location.pathname;

	/*!
	 * Declare the steps of the help guide
	*/
	siteHelp.addSteps([
		// step 1
		{
			intro: '<h3>Welcome to Boatbreakers</h3>Welcome to our interactive tour, which will provide you with help for each of the different elements that appear on screen. You can access it at any time from the Main menu or by clicking on a <i class="fas fa-question-circle fa-fw"></i>, which will show you help for that section.'
		},

		// step 2
		{
			element: '#telephone',
			intro: '<h3>Telephone</h3>This is our contact number, clicking on the number will allow you to call us.',
			position: 'bottom'
		},

		// step 3
		{
			element: '#site-nav',
			intro: '<h3>Navigation Bar</h3>This is the navigation bar, use this to navigate to the different sections of the website.',
			position: 'bottom'
		}
	]);

	/*!
	 * Build Steps based on the page url.
	 */
	// home page
	if (url == '/') {
		siteHelp.addSteps([
			// step 4
			{
				element: '#home-header-row',
				intro: '<h3>Welcome</h3>This is the Welcome Header. It provides a brief introduction and a quick link. Link varies depending on if you have logged in or not.'
			}
		]);
	}

	// login page
	if (url.indexOf('/accounts/login/') === 0) {
		siteHelp.addSteps([
			// step 4
			{
				element: '#username-block',
				intro: '<h3>Username</h3>Enter your username into this box. A username is must be a valid e-mail address'
			},

			// step 5
			{
				element: '#password-block',
				intro: '<h3>Password</h3>Enter your password into this box.'
			},

			// step 6
			{
				element: '#submit-block',
				intro: '<h3>Submit</h3>Press this button to login.'
			},

			// step 7
			{
				element: '#not-registered',
				intro: '<h3>Not Registered</h3>Not registered for the site yet? Click here to start the registration process'
			}
		]);
	}

	// registration page
	if (url == '/accounts/register/') {
		siteHelp.addSteps([
			// step 4
			{
				element: '#name-fields',
				intro: '<h3>Your Name</h3>This section will collect details about you. Your Title (optional), First and Last Name (required fields)'
			},

			// step 5
			{
				element: '#address-fields',
				intro: '<h3>Address</h3>This section collects your address details. You can use the <b>Postcode Lookup</b> field to find your address and populate the address fields automatically.'
			},

			// step 6
			{
				element: '#contact-fields',
				intro: '<h3>Contact Details</h3>This section collects your e-mail address and telephone number. The e-mail address will also act as your username.'
			},

			// step 7
			{
				element: '#password-fields',
				intro: '<h3>Password</h3>This section allows you to set a password. An on-screen guide will help you pick a strong password.'
			},

			// step 8
			{
				element: '#register_submit',
				intro: '<h3>Register Button</h3>Use this button to register for the site. If your registration is successful, you will be automatically logged in and re-directed to the My Account page.'
			}
		]);
	}

	// my account page
	if (url == '/accounts/') {
		siteHelp.addSteps([
			// step 4
			{
				intro: '<h3>Your Account</h3>This is your account home page, from here you can quickly access any quotes you have submitted, as well as see if you have any messages waiting for you to look at.'
			}
		]);
	}

	// new/edit scrap enquiry
	if (url == '/quote/new/' || url.indexOf('/quote/edit/') === 0) {
		siteHelp.addSteps([
			// step 4
			{
				element: '#boat-type-fields',
				intro: '<h3>Type of Boat</h3>This section gathers the type of boat and the keel type of the boat you are having scrapped. This information is used to form the basis of your quote. The Keel type of the boat effects the type of transportation needed to move the boat.'
			},
			// step 5
			{
				element: '#boat-detail-fields',
				intro: '<h3>Boat Details</h3>This section collects more information about the boat: <ul><li><b>Length:</b> The length of the boat. You can specify feet or metres for the length, it will automatically be converted to feet for you.</li><li><b>Weight:</b> The weight of the boat in tonnes or kilograms.</li><li><b>Hull Material:</b> What type of material is the boat made from?</li><li><b>Hazardous Materials:</b>What hazardous waste is left on the boat? For example; if there is an engine still on the boat, then Engine Oil will be present. If you are unsure, just select Unknown.</li></ul>',
				position: 'bottom'
			},
			// step 6
			{
				element: '#engine-fields',
				intro: '<h3>Engine Details</h3>This section collects more information about the engine (if any) that is on the boat. Most of this information is optional and can be left out. If the engine has been removed, simple select removed from the drop down.'
			},
			// step 7
			{
				element: '#location-fields',
				intro: '<h3>Boat Location</h3>This section collects details about the boats current location: <ul><li><b>Boats Postcode:</b> The postcode of the location the boat is currently stored. You can use the address lookup field to search for the postcode if you don\'t know it. The postcode is used to work out the estimated travel distance.</li><li><b>Scrap at Location:</b>Do you want us/or will we have to scrap the boat where it\'s located? This is a more costly solution and we prefer, when ever possible, to simply collect the boat and move it to our yard for disposal.</li><li><b>Still in the water?</b>Is the boat still in the water or has it been lifted out and is waiting transportation?</li><li><b>Access to a Trailer?</b>Does the boat have access to a trailer that can be used to move it? Please note, boats over 24 feet cannot be towed and specialist transportation will need to be arranged.</li></ul>'
			},
			// step 8
			{
				element: '#additional-info-fields',
				intro: '<h3>Additional Information</h3>This optional section is provided for you to supply any additional information you think we may need about the boat.'
			},
			// step 9
			{
				element: '#privacy-fields',
				intro: '<h3>Privacy</h3>This section informs you of your privacy rights and what we will do with the data we have collected. This is required of us by law and you will not be able to submit the form unless you give us your consent to use the information provided to process your request.'
			},
			// step 10
			{
				element: '#submit-form',
				intro: '<h3>Submit Form</h3>Once all the required fields have been filled out, you will be able to submit the form using this button.'
			},
		]);
	}

	// view quote
	if (url.indexOf('/quote/view/') === 0) {
		siteHelp.addSteps([
			// step 4
			{
				element: '#ref-block',
				intro: '<h3>Reference</h3>This section shows you some references relating to the quote. <ul><li><b>Quote Number:</b> This is the reference number you will need if you make any telephone enquiries about the quote.</li><li><b>Date:</b> The date you submitted this quote.</li><li><b>Latest Activity:</b> This is a last action that was taken on your quote. You can click on the \'View Log\' link to view a full history</li></ul>'
			},
			// step 5
			{
				element: '#options-block',
				intro: '<h3>Options</h3>This section will provide you with some links to preform various tasks on your quote, from allowing you to edit it, or decline it should you no longer wish to use our services.'
			},
			// step 6
			{
				element: '#quote-block',
				intro: '<h3>Quote</h3>This section will show you the prices for the two services we offer. <ul><li><b>All Inclusive:</b> With our All Inclusive service, we will come and collect your boat, transport it to our yard and dispose of her for one fixed price.</li><li><b>Disposal Only:</b> With our disposal only service, you can save money on the transportation costs by delivering the boat to us, either by road or by sea.</li></ul>'
			},
			// step 7
			{
				element: '#summary-block',
				intro: '<h3>Summary</h3>This section contains a summary of your quote submission.'
			},
			// step 8
			{
				element: '#messages-block',
				intro: '<h3>Messages</h3>This section shows you any messages and responses you have received and allow you to respond. Please note: New messages cannot be sent if you have declined the quote'
			},
			// step 9
			{
				element: '#images-block',
				intro: '<h3>Images</h3>This section will allow you to upload any pictures you have of the boat and its surroundings. You can simply drag and drop images into the grey box or press the Upload a file button. Please note: Once a quote has been paid or declined, you will no longer be able to upload images.'
			},
		]);
	}

	// add a message
	if (url.indexOf('/quote/messages/new/') === 0) {
		siteHelp.addSteps([
			// step 4
			{
				intro: "Use this box to send us a message and press the submit button when finished."
			}
		]);
	}

	// quote activity log
	if (url.indexOf('/quote/activity_log/') === 0) {
		siteHelp.addSteps([
			// step 4
			{
				intro: "This page shows you a history of all the activity that has happened on your quote so far."
			}
		]);
	}


	/*!
	 * Set the options used buy the Help Guide
	 */
	 siteHelp.setOptions({
	 	showProgress: true,
	 	skipLabel: 'Exit Help'
	 })

	/*!
	 * Evaluate the stepNumber provided by the function call.
	 * if 0, start the guide from the start.
	 */
	 if (stepNumber == 0) {
	 	// start the guide from the beginning.
	 	siteHelp.start();
	 } else {
	 	// jump to the step number.
	 	siteHelp.start().goToStep(stepNumber);
	 }
}