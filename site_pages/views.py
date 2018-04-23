# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# generate the home page
def get_home_page(request):
	args = {
		'pageTitle' : 'Welcome to Boatbreakers',
		'homePage' : True
	}
	return render(request, 'pages/index.html', args)


# generate the contact us page.
def get_contact_us_page(request):

	# page arguments
	args = {
		'pageTitle': 'Contact Us',
	}
	return render(request, 'pages/contact_us.html', args)
