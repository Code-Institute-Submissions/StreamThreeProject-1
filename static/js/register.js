$(document).ready(function() {
	// generate the postcode lookup field and set the fields to populate.
	$('#lookup_field').setupPostcodeLookup({
		api_key: 'iddqd',
		output_fields: {
			line_1: '#id_address_line_1',  
			line_2: '#id_address_line_2',         
			post_town: '#id_address_town',
			postal_county: '#id_address_county',
			postcode: '#id_post_code'
		},
		input: '#postcode_lookup',
		button: '#doLookup',
		dropdown_class: 'form-control'
	});
});