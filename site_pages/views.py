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
