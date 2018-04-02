# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


from .forms import UserRegistrationForm, UserLoginForm
from .models import User

# create the user registration view
def register(request):

	# if request method is POST
	if request.method == 'POST':

		# get the form data
		form = UserRegistrationForm(request.POST)

		# if the form is valid
		if form.is_valid():
			# save the form
			form.save()

			# authenticate the user
			user = auth.authenticate(email=request.POST.get('email'),
									 password=request.POST.get('password1'))

			# if the user authenticated successfully
			if user:
				# set a success message
				messages.success(request, "Congratulations! You have successfully registered")

				# login the user and redirect to their profile page
				auth.login(request, user)
				return redirect(reverse('my_account'))

			# if user did not authenticate
			else:
				# set error message
				messages.error(request, "Sorry, you are unable to log in at this time, please try again")

	# if not a form POST, display the form
	else:
		# show registration form.
		form = UserRegistrationForm()

	# page arguments
	args = { 
		'form': form, # form to pass to template
		'pageTitle': 'Register' # page title
	}  
	args.update(csrf(request))  # csrf token to use on form.

	# render the form.
	return render(request, 'user_accounts/register.html', args)


def login(request):

	# if request is a POST, process the form.
	if request.method == 'POST':

		# get form data.
		form = UserLoginForm(request.POST)

		# if form is valid.
		if form.is_valid():

			# authenticate the user.
			user = auth.authenticate(email=request.POST.get('email'),
									 password=request.POST.get('password'))

 			# if the user authenticated successfully, log them in.
			if user is not None:
				# log in
				auth.login(request, user)

				# display success message.
				messages.success(request, "You have successfully logged in")

				# redirect to account page.
				return redirect(reverse('my_account'))

			# if not a valid user.
			else:
				
				# display error message
				form.add_error(None, "Your email or password was not recognised")
 
	else:
		form = UserLoginForm()
 	
 	# page arguments
	args = {
		'form' : form,
		'pageTitle': 'Please Log In'
	}
	args.update(csrf(request))

	return render(request, 'user_accounts/login.html', args)


# log out the current user.
def logout(request):
	# log out user.
	auth.logout(request)

	# add logout message
	messages.success(request, "You have successfully logged out")

	# return to home page.
	return redirect(reverse('home'))


# my account page.
@login_required(login_url='/account/login/')
def my_account(request):

	# page arguments.
	args = {'pageTitle': 'My Account'}

	return render(request, 'user_accounts/my_account.html', args)


# lookup to check if the e-mail address is already in use. Ajax call from the registration page. 
def lookup_email(request):

	# if a GET request is made
	if request.is_ajax() and request.method == "GET":
		username = request.GET.get('username', None)

		data = {
			'is_taken' : User.objects.filter(email__iexact=username).exists()
		}

		return JsonResponse(data)
