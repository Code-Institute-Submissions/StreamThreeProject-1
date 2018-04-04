# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from tinymce.models import HTMLField


# Creates the Scrap Quotes Model.
class Quote(models.Model):

	# choices for the type_of_boat field.
	BOAT_TYPE_CHOICES = (
		(None, 'Please select the type of boat'),
		('Sailing Dinghy', 'Sailing Dinghy'),
		('Motor Boat', 'Motor Boat'),
		('Yacht', 'Yacht'),
		('Narrowboat', 'Narrowboat')
	)

	# choices for the keel_type field.
	KEEL_TYPES = (
		('N/A', 'Not Applicable'),
		('Fin Keel', 'Fin Keel'),
		('Bilge Keel', 'Keel'),
		('Other', 'Other')
	)

	# choices for the hull_material field.
	HULL_MATERIALS = (
		(None, 'Please select the material the hull is made from'),
		('Aluminium', 'Aluminium'),
		('Carbon Fibre', 'Carbon Fibre'),
		('Ferro Cement', 'Ferro Cement'),
		('GRP / Fibreglass', 'GRP / Fibreglass'),
		('Plastic', 'Plastic'),
		('Steel', 'Steel'),
		('Wood', 'Wood')
	)

	# choices for hazardous_mats field.
	HAZARDOUS_MATERIALS = (
		('Asbestos', 'Asbestos'),
		('Petrol', 'Petrol'),
		('Diesel', 'Diesel'),
		('Gas', 'Gas'),
		('Waste Tanks', 'Waste Tanks'),
		('Explosives', 'Explosives'),
		('Engine Oil', 'Engine Oil'),
		('Unknown', 'Unknown')
	)

	# choices for any yes/no/don't know field.
	YES_NO_DONT_KNOW = (
		('Yes', 'Yes'),
		('No', 'No'),
		('Don\'t Know', 'Don\'t Know')
	)

	# choices for the type_of_engine field.
	ENGINE_TYPE = (
		(None, 'Please select the type of engine.'),
		('Outboard', 'Outboard'),
		('Inboard', 'Inboard'),
		('Twin Outboard', 'Twin Outboard'),
		('Twin Inboard', 'Twin Inboard'),
		('Other', 'Other')
	)

	# choices for boat_in_water field.
	BOAT_IN_WATER_CHOICES = (
		(None, 'Please select if your boat is in the water.'),
		('No', 'No'),
		('Yes, along side and ready to be lifted', 'Yes, along side and ready to be lifted'),
		('Yes, needs moving and lifting out', 'Yes, needs moving and lifting out')
	)

	# identification fields
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="quotes")  # ID of the User who created this quote.
	created_at = models.DateTimeField(auto_now_add=True) # The day they created it.
	ip_address = models.GenericIPAddressField(protocol='IPv4')  # IP Address of the person who sent in the quote.

	# quote fields.
	type_of_boat = models.CharField(max_length=20, null=False, blank=False, choices=BOAT_TYPE_CHOICES)  # the type of boat being scrapped.
	keel_type = models.CharField(max_length=10, null=False, blank=False, choices=KEEL_TYPES)  # what type of keel does the boat have.
	boat_length = models.PositiveSmallIntegerField(null=False, blank=False)  # overall length of the boat in feet.
	boat_weight = models.PositiveSmallIntegerField(null=False, blank=False)  # weight of the boat in tonnes.
	hull_material = models.CharField(max_length=20, null=False, blank=False)  # what material is the boats hull made from.
	hazardous_mats = models.CharField(max_length=100, blank=True)  # multi-select fields, what hazardous material is left on the boat.
	engine_removed = models.CharField(max_length=10, null=False, blank=False, choices=YES_NO_DONT_KNOW)  # has the engine been removed?
	type_of_engine = models.CharField(max_length=15, blank=True, choices=ENGINE_TYPE)  # what type of engine has the boat got?
	engine_make = models.CharField(max_length=50, blank=True)  # what make is the engine?
	engine_cylinders = models.PositiveSmallIntegerField(blank=True)  # how many cylinders
	engine_hours = models.PositiveSmallIntegerField(blank=True)  # how long has the engine been used.
	engine_still_run = models.CharField(max_length=10, blank=True, choices=YES_NO_DONT_KNOW)  # does the engine still run?
	boat_in_water = models.CharField(max_length=40, blank=True, choices=BOAT_IN_WATER_CHOICES)  # is the boat still in the water?
	has_trailer = models.CharField(max_length=10, blank=True, choices=YES_NO_DONT_KNOW)  # does the boat have a trailer?
	trailer_road_legal = models.CharField(max_length=10, blank=True, choices=YES_NO_DONT_KNOW)  # is the trailer road legal?
	travel_distance = models.PositiveSmallIntegerField(blank=True)  # estimated travel distance to the boat
	additional_info = HTMLField()  # anything extra that might be needed about the boat.

	# consent
	my_consent = models.BooleanField(default=False)  # a record of the user's consent to be contacted.

	# admin fields
	approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, limit_choices_to={'is_staff': True })  # who approved the quote?
	date_approved = models.DateTimeField(blank=True)

	# quote totals
	all_inclusive_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	scrap_only_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	all_inclusive_monthly = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	scrap_only_monthly = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	# last updated
	updated = models.DateTimeField(auto_now=True)  # date and time of the last update made to the quote.


	def __unicode__(self):
		return "{0}ft - {1}".format(self.boat_length, self.type_of_boat)


# Model to hold uploaded images by the user relating to the quote.
class QuoteImages(models.Model):

	# fields.
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="quote_images")
	quote = models.ForeignKey(Quote, related_name="quote_images")
	height = models.PositiveSmallIntegerField()
	width = models.PositiveSmallIntegerField()
	file_path = models.ImageField(upload_to='%Y/%m/%d/', height_field=height, width_field=width)


	# return the path.
	def __unicode__(self):
		return file_path
