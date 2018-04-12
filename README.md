# "Scrap a Boat" Quotation Management System.

## Brief

The company I currently work for specialises in buying, selling and disposing of boats. We currently have a ['Scrap Calculator'](http://www.boatbreakers.com/scrap-a-boat/scrap-your-boat/) in place already, which is functional but has many limitations. The goal of my project is to re-develop the existing system into something which is easy to use and provides a lot more features.

## Project Functionality

* User Management
	* Allow Users to Register to the website
	* Allow Users to Login and Logout of the website
	* Allows Users to edit their personal information
* Quote System
	* End Users:
		* Allow users to generate a quote to scrap their boat
		* Allow users to edit a quote after it's been created
		* Allow users to view the quote.
			* Allow users to submit images related to their quote on-line
			* Allow users to chat to staff about the quote on-line
			* Allow the user to accept or decline a quote that has been approved.
			* Allow the user to pay on-line, either by paying the full amount up-front, or setting up a 10 month payment plan.
			* Allow the user to track the status of the quote on-line.
	* Staff Members:
		* Allow staff members to view quotes
		* Allow staff members to edit quotes
		* Allow staff members to create quotes and assign them to a user
		* Allow staff members to approve a quote - once approved, the quote will no longer be editable and the end user has the options to accept the quote and pay on-line, or close the quote to show they are not interested.
		* Allow staff members to update the status of a quote.

## Technology Used

* HTML5
* CSS3
	* [Bootstrap 3.3](https://getbootstrap.com/docs/3.3/) - Used for the responsive layout of the site.
* JavaScript
	* jQuery 3.3.1
		* [Fancybox 3.3.4](http://fancyapps.com/fancybox/3/) - Used to display user submitted images in a gallery.
		* [Ideal Postcodes](https://ideal-postcodes.co.uk) - Used to add Postcode and Address Lookup features to the site.
		* [jQuery Password Strength Meter](https://github.com/ablanco/jquery.pwstrength.bootstrap) - Used to show a password strength meter on the registration page.
		* [IntroJS](https://introjs.com) - Used to add help guides to various pages and forms.
		* [FileUploader](https://github.com/skoczen/django-ajax-uploader) - Used to add AJAX image uploading.
		* [TinyMCE](https://www.tinymce.com/download/) - Used to add Rich Text editor capabilities to text fields.
* Python
	* [Django 1.11.11](https://www.djangoproject.com)
	* [Google Maps 2.5.1](https://github.com/googlemaps/google-maps-services-python) - Used to preform distance calculations between two postcodes as part of the scrap quotation.
	* [Django TinyMCE 2.7.0](https://github.com/aljosa/django-tinymce) - Used to add TinyMCE to Django.

## Testing

## Deployment 