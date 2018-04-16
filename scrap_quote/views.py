# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from decimal import *
import math
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.conf import settings 
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib import messages

import googlemaps
from ajaxuploader.views import AjaxFileUploader
import stripe

from .forms import QuotationForm, PayForQuoteForm
from .models import Quote, QuoteImages, QuoteLog, QuoteLogStatus


# set up stripe
stripe.api_key = settings.STRIPE_SECRET


# AJAX Image Uploader object.
import_uploader = AjaxFileUploader()


# View to handle new scrap quoations.
@login_required()
def new_quotation(request):

	# if a POST is made.
	if request.method == 'POST':

		# get the form and form data.
		form = QuotationForm(request.POST)

		# check the form is valid.
		if form.is_valid():

			# capture the form details.
			quote = form.save(commit=False)

			# update hidden fields with information
			if not request.user.is_staff:
				quote.user = request.user
			
			quote.ip_address = request.META['REMOTE_ADDR']
			quote.travel_distance = get_distance(quote.boat_location)

			# save the form
			quote.save()  # save the quote data
			form.save_m2m()  # save the many-to-many hazardous materials data.

			# do the scrap calculation.
			do_scrap_calculation(quote.pk)

			# create log entry - created
			logEntry = QuoteLog(quote=Quote.objects.get(pk=quote.pk), user=request.user, status=QuoteLogStatus.objects.get(pk=1), ip_address=request.META['REMOTE_ADDR'])
			logEntry.save()

			# redirect to view quotation page
			return redirect(reverse('view_quote', args=[quote.pk]))

	else:

		# show the form
		form = QuotationForm()

	# page arguments
	args = {
		'pageTitle': 'Get a Scrap Quotation',
		'form': form
	}
	args.update(csrf(request))  # csrf token to use on form.

	# render page
	return render(request, 'scrap_quote/quotation_form.html', args)


# function to preform the scrap calculation and return the results in a dictionary.
def do_scrap_calculation(quote_id):

	# get the quote
	quote = get_object_or_404(Quote, pk=quote_id)

	# initialise variables.
	hazardous_mats_cost = Decimal(0)
	location_cost = Decimal(0)
	crane_cost = Decimal(0)

	# set constants to hold basic price information used in calculations.
	WEIGHT_COST = Decimal(170)  # the base price per tonne.
	DELIVERY_COST = Decimal(0.45)  # the base price per mile.

	# get the basic scrap price, based on length of boat and type of boat
	# if a sailing dinghy is selected, disregard the length and weight fields and use base cost.
	if quote.type_of_boat.cost == 199:
		base_scrap_cost = quote.type_of_boat.cost
	# if boat length is less than 18 feet and base cost is greater than 199
	elif quote.boat_length <= 18 and quote.type_of_boat.cost > 199:
		base_scrap_cost = Decimal(599)  # set the base scrap price to 599

	# if boat length is between 18 and 21 feet long
	elif quote.boat_length > 18 and quote.boat_length <= 21:
		base_scrap_cost = Decimal(790)  # set the base scrap price to 790

	# if boat length multiplied by length_cost is less than base cost
	elif quote.boat_length * quote.hull_material.cost < quote.type_of_boat.cost:
		base_scrap_cost = quote.type_of_boat.cost

	# else, set cost to boat length multiplied by length_cost plus weight multiplied by weight_cost
	else:
		base_scrap_cost = (quote.boat_length * quote.hull_material.cost) + (quote.boat_weight * WEIGHT_COST) + quote.keel_type.cost

	# get the cost of the hazardous materials if any.
	if quote.hazardous_mats.all().exists():

		# loop through the list and add the hazardous materials together.
		for mat in quote.hazardous_mats.all(): 
			hazardous_mats_cost += Decimal(mat.cost)

	# if scrap on location, work out how many days it'll take
	if quote.scrap_at_location.cost > 1:
		
		# if boat is over 30 feet long
		if quote.boat_length > 30:

			# calculate the estimated duration of the job, and take the ceiling value.
			_duration = Decimal(math.ceil(quote.boat_length / 30))
		else:

			# else, set the duration to 1 day.
			_duration = Decimal(1)

		# calculate the scrap at location cost.
		location_cost = Decimal(_duration * quote.scrap_at_location.cost)

	# calculate the travel cost (cost includes the return journey)
	travel_distance_cost = Decimal(math.ceil((quote.travel_distance * DELIVERY_COST) * 2))

	# if boat is over 24 feet long, add crane hire to all inclusive total
	if quote.boat_length > 24:
		crane_cost = Decimal(750)

	# calculate the totals
	all_inclusive_grand_total = Decimal(base_scrap_cost + hazardous_mats_cost + 
								quote.engine.cost + location_cost + travel_distance_cost +
								quote.boat_in_water.cost + quote.has_trailer.cost + crane_cost)
	scrap_only_grand_total = Decimal(base_scrap_cost + hazardous_mats_cost + 
								quote.engine.cost)

	# calculate the monthly totals, set to 0 if grand totals are less than £350.
	if all_inclusive_grand_total > Decimal(350):
		all_inclusive_monthly_total = Decimal(all_inclusive_grand_total / 10)  # 10 monthly payments.
	else:
		all_inclusive_monthly_total = Decimal(0)

	if scrap_only_grand_total > Decimal(350):
		scrap_only_monthly_total = Decimal(scrap_only_grand_total / 10)  # 10 monthly payments.
	else:
		scrap_only_monthly_total = Decimal(0)

	# save the values to the database.
	quote.all_inclusive_total = all_inclusive_grand_total
	quote.all_inclusive_monthly = all_inclusive_monthly_total
	quote.scrap_only_total = scrap_only_grand_total
	quote.scrap_only_monthly = scrap_only_monthly_total

	# save the record.
	quote.save()


# get the total distance travelled.
def get_distance(post_code):

	# load google maps
	gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)

	# do the distance matrix lookup, between the clients postcode to the location of our yard.
	distance = gmaps.distance_matrix(post_code, 'PO28QA')

	# return the ceiling value divided by 1609 (number of metres in a mile)
	return math.ceil(distance['rows'][0]['elements'][0]['distance']['value'] / 1609)


# view the quotation.
@login_required()
def view_quotation(request, quote_id):
	quote = get_object_or_404(Quote, pk=quote_id)
	quoteImages = QuoteImages.objects.filter(quote=quote_id)
	quoteStatus = QuoteLog.objects.filter(quote=quote_id).order_by('created_at').last()

	# check the quote belongs to the user, or is a member of staff viewing it.
	if quote.user == request.user or request.user.is_staff:
		args = {
			'quote' : quote,
			'images' : quoteImages,
			'statusUpdate' : quoteStatus,
			'pageTitle' : 'View Quotation',
		}

		# render the quote.
		return render(request, 'scrap_quote/view_quotation.html', args)

	else:

		# display error message.
		return render(request, 'scrap_quote/not_your_quote.html')


# edit the quotation.
@login_required()
def edit_quotation(request, quote_id):
	
	# get the quote.
	quote = get_object_or_404(Quote, pk=quote_id)

	# check if the quote belongs to the user or a staff member is editing it.
	if quote.user == request.user or request.user.is_staff:

		# check that the quote has not been paid or declined.
		if not quote.is_paid or not quote.is_declined:
		
			# if a POST is made.
			if request.method == 'POST':

				# get the form and form data.
				form = QuotationForm(request.POST, instance=quote)

				# check the form is valid.
				if form.is_valid():
					# capture the form details.
					quote = form.save(commit=False)

					# if not a staff member, updated these fields.
					if not request.user.is_staff:
						quote.is_approved = False  # set the quote to un-approved again.
					
					# update the travel distance
					quote.travel_distance = get_distance(quote.boat_location)

					# save the form
					quote.save()  # save the quote data
					form.save_m2m()  # save the many-to-many hazardous materials data.

					# do the scrap calculation.
					do_scrap_calculation(quote.pk)

					# create log entry - edited
					logEntry = QuoteLog(quote=Quote.objects.get(pk=quote.pk), user=request.user, status=QuoteLogStatus.objects.get(pk=2), ip_address=request.META['REMOTE_ADDR'])
					logEntry.save()

					# return to view quotation page.
					return redirect(view_quotation, quote.pk)

			else:

				# show the form
				form = QuotationForm(instance=quote)

		# if it's been approved
		else:
			# return to view quotation page.
			return redirect(view_quotation, quote.pk)

		args = {
			'pageTitle' : 'Edit Quotation',
			'is_edit' : True,
			'quote_id' : quote.pk,
			'form' : form 
		}
		args.update(csrf(request))

		return render(request, 'scrap_quote/quotation_form.html', args)

	# if invalid user.
	else:

		# display error message.
		return render(request, 'scrap_quote/not_your_quote.html')


# View to handle Staff Members approving a quote.
@login_required
def approve_quotation(request, quote_id):
	# get the quote.
	quote = get_object_or_404(Quote, pk=quote_id)

	# if user is a staff member and quote is not declined.
	if request.user.is_staff and not quote.is_declined:

		# update the quote to show as approved.
		quote.is_approved = True
		quote.approved_by = request.user
		quote.date_approved = timezone.now()

		# save the quote.
		quote.save()

		# create log entry - approved
		logEntry = QuoteLog(quote=Quote.objects.get(pk=quote.pk), user=request.user, status=QuoteLogStatus.objects.get(pk=3), ip_address=request.META['REMOTE_ADDR'])
		logEntry.save()

		# return the the view quotation page.
		return redirect(view_quotation, quote.pk)

	# if not a staff member, do nothing and just return the view quotation page.
	return redirect(view_quotation, quote.pk)


# View to handle a user declining a quote which has been approved.
@login_required
def decline_quotation(request, quote_id):
	# get the quote.
	quote = get_object_or_404(Quote, pk=quote_id)

	# if user is a staff member and quote is not declined.
	if quote.user == request.user and not quote.is_paid:

		# update the quote to show as approved.
		quote.is_declined = True
		quote.date_declined = timezone.now()

		# save the quote.
		quote.save()

		# create log entry - declined
		logEntry = QuoteLog(quote=Quote.objects.get(pk=quote.pk), user=request.user, status=QuoteLogStatus.objects.get(pk=6), ip_address=request.META['REMOTE_ADDR'])
		logEntry.save()

		# return the the view quotation page.
		return redirect(view_quotation, quote.pk)

	# if not a staff member, do nothing and just return the view quotation page.
	return redirect(view_quotation, quote.pk)


# view to show the activity log of a quote.
@login_required
def quote_activity_log(request, quote_id):

	# get the quote.
	quote = get_object_or_404(Quote, pk=quote_id)

	# check if the quote belongs to the user or a staff member is editing it.
	if quote.user == request.user or request.user.is_staff:

		# get the activity log
		log = QuoteLog.objects.filter(quote=quote_id).order_by('-created_at')

		args = {
			'quoteLog' : log,
			'quote_id' : quote_id,
			'pageTitle' : 'Quote: BB-SCRAP-{0:0>5} Activity Log'.format(quote_id),
		}

		# render the quote.
		return render(request, 'scrap_quote/quote_log.html', args)

	else:

		# display error message.
		return render(request, 'scrap_quote/not_your_quote.html')


# view to handle paying for a quote.
@login_required
def pay_quotation(request, quote_id, payment_type):

	# get the quote.
	quote = get_object_or_404(Quote, pk=quote_id)

	# check if the quote belongs to the user.
	if quote.user == request.user:

		# check that the quote has not been paid or declined.
		if not quote.is_paid and not quote.is_declined:

			# create a dictionary to hold the costs.
			amount_to_pay = {
				'all' : {
					'amount' : quote.all_inclusive_total,
					'payable' : int(str(quote.all_inclusive_total).replace('.', '')),
					'status' : 'All Inclusive',
					'code' : 'a'
				},
				'disposal' : {
					'amount' : quote.scrap_only_total,
					'payable' : int(str(quote.scrap_only_total).replace('.', '')),
					'status' : 'Disposal Only',
					'code' : 'd'
				}
			}
		
			# if a POST is made.
			if request.method == 'POST':

				# get the form and form data.
				form = PayForQuoteForm(request.POST)

				# check the form is valid.
				if form.is_valid():

					# try and create a stripe customer.
					try:
						# create the charge.
						customer = stripe.Charge.create(
							amount=amount_to_pay[payment_type]["payable"],
							currency="GBP",
							description=quote.user.email,
							card=form.cleaned_data['payment_id'],
						)

						# if the payment goes through
						if customer.paid:

							# update the quote to show as paid and the date paid.
							quote.is_paid = True
							quote.payment_type = amount_to_pay[payment_type]["code"]
							quote.payment_id = form.cleaned_data['payment_id']
							quote.date_paid = timezone.now()

							# save the quote.
							quote.save()

							# create log entry - paid
							logEntry = QuoteLog(
								quote=Quote.objects.get(pk=quote.pk), 
								user=request.user, 
								status=QuoteLogStatus.objects.get(pk=5), 
								comment="Thankyou, a payment for our {0} service in the amount of £{1}.00 has been made by".format(amount_to_pay[payment_type]["status"], amount_to_pay[payment_type]["amount"]), 
								ip_address=request.META['REMOTE_ADDR']
							)
							logEntry.save()

							# return to view quotation page.
							return redirect(view_quotation, quote.pk)

						# if an error occurs.
						else:
							messages.error(request, "We have been unable to take payment with that card, please try again or use a different card.")

					# if a card error occurs.
					except stripe.error.CardError, e:
						messages.error(request, "Your card has been declined.")
			
			# if not a post.
			else:

				# show the form
				form = PayForQuoteForm()

		# if it's been paid, or declined
		else:
			# return to view quotation page.
			return redirect(view_quotation, quote.pk)

		args = {
			'pageTitle' : 'Pay For Quotation: BB-SCRAP-{0:0>5}'.format(quote.pk),
			'quoteAmount' : amount_to_pay[payment_type]["amount"],
			'form' : form,
			'publishable' : settings.STRIPE_PUBLISHABLE,
			'service' : amount_to_pay[payment_type]["status"],
			'quote_id' : quote.pk
		}
		args.update(csrf(request))

		return render(request, 'scrap_quote/pay_for_quotation.html', args)

	# if invalid user.
	else:

		# display error message.
		return render(request, 'scrap_quote/not_your_quote.html')
