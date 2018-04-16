# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.dispatch import receiver

from ajaxuploader.views import AjaxFileUploader
from ajaxuploader.signals import file_uploaded
from tinymce.models import HTMLField


# Boat Type Model
class TypeOfBoat(models.Model):

	# fields
	type_of_boat = models.CharField(max_length=20)
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the type of boat
	def __unicode__(self):
		return self.type_of_boat

	# class meta for the admin section.
	class Meta:
		verbose_name = 'Type of Boat'
		verbose_name_plural = 'Type of Boat'


# Keel Types Model
class TypeOfKeel(models.Model):

	# fields
	type_of_keel = models.CharField(max_length=20)
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the type of keel
	def __unicode__(self):
		return self.type_of_keel

	# class meta for the admin section.
	class Meta:
		verbose_name = 'Type of Keel'
		verbose_name_plural = 'Type of Keel'


# Hull Material Model
class HullMaterials(models.Model):

	# fields
	hull_material = models.CharField(max_length=30)
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the hull material name
	def __unicode__(self):
		return self.hull_material

	# class meta for the admin section
	class Meta:
		verbose_name = 'Hull Material'
		verbose_name_plural = 'Hull Materials'


# Hazardous Materials Model
class HazardousMaterials(models.Model):

	# fields
	mat_type = models.CharField(max_length=50)
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the material name
	def __unicode__(self):
		return self.mat_type

	# class meta for the admin screen
	class Meta:
		verbose_name = 'Hazardous Material'
		verbose_name_plural = 'Hazardous Materials'


# Engine Types Model
class EngineTypes(models.Model):

	# fields
	engine_type = models.CharField(max_length=20)
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the type of engine
	def __unicode__(self):
		return self.engine_type

	# class meta for the admin screen.
	class Meta:
		verbose_name = 'Engine Type'
		verbose_name_plural = 'Engine Types'


# Engine Still Run Model
class EngineStillRun(models.Model):

	# fields
	engine_still_run = models.CharField(max_length=50)
	is_disabled = models.BooleanField(default=False)

	# return the engine still run text
	def __unicode__(self):
		return self.engine_still_run

	# class meta for the admin screen.
	class Meta:
		verbose_name = 'Engine Still Run Option'
		verbose_name_plural = 'Engine Still Run Options'


# Boat in the Water Options
class BoatInWaterOptions(models.Model):

	# fields
	is_in_water = models.CharField(max_length=40)
	cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the boat in water option
	def __unicode__(self):
		return self.is_in_water

	# class meta for the admin screen.
	class Meta:
		verbose_name = 'Boat in Water Option'
		verbose_name_plural = 'Boat in Water Options'


# Trailer Options Model
class TrailerOptions(models.Model):

	# fields
	trailer_option = models.CharField(max_length=40)
	cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the trailer option
	def __unicode__(self):
		return self.trailer_option

	# class meta for the admin screen.
	class Meta:
		verbose_name = 'Trailer Option'
		verbose_name_plural = 'Trailer Options'


# Scrap at Location model
class ScrapAtLocation(models.Model):

	# fields
	scrap_at_location = models.CharField(max_length=40)
	cost = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	is_disabled = models.BooleanField(default=False)

	# return the scrap at location text
	def __unicode__(self):
		return self.scrap_at_location

	# class meta for the admin screen
	class Meta:
		verbose_name = 'Scrap At Location Option'
		verbose_name_plural = 'Scrap At Location Options'


# Creates the Scrap Quotes Model.
class Quote(models.Model):

	PAYMENT_MADE_OPTIONS = (
		('a', 'All Inclusive'),
		('d', 'Disposal Only')
	)

	# identification fields
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="quotes")  # ID of the User who created this quote.
	created_at = models.DateTimeField(auto_now_add=True) # The day they created it.
	ip_address = models.GenericIPAddressField(protocol='IPv4')  # IP Address of the person who sent in the quote.

	# quote fields.
	type_of_boat = models.ForeignKey(TypeOfBoat, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False })  # the type of boat being scrapped.
	keel_type = models.ForeignKey(TypeOfKeel, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False })  # what type of keel does the boat have.
	boat_length = models.PositiveSmallIntegerField(null=False, blank=False)  # overall length of the boat in feet.
	boat_weight = models.PositiveSmallIntegerField(null=False, blank=False)  # weight of the boat in tonnes.
	hull_material = models.ForeignKey(HullMaterials, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False })  # what material is the boats hull made from.
	hazardous_mats = models.ManyToManyField(HazardousMaterials, blank=True)  # multi-select fields, what hazardous material is left on the boat.
	engine = models.ForeignKey(EngineTypes, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False })  # what type of engine has the boat got?
	engine_make = models.CharField(max_length=50, blank=True)  # what make is the engine?
	engine_cylinders = models.PositiveSmallIntegerField(blank=True, null=True)  # how many cylinders
	engine_hours = models.PositiveSmallIntegerField(blank=True, null=True)  # how long has the engine been used.
	engine_still_run = models.ForeignKey(EngineStillRun, on_delete=models.SET_NULL, blank=True, null=True, limit_choices_to={ 'is_disabled' : False })  # does the engine still run?
	scrap_at_location = models.ForeignKey(ScrapAtLocation, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False })  # can we scrap the boat where it's located?
	boat_in_water = models.ForeignKey(BoatInWaterOptions, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False })  # is the boat still in the water?
	has_trailer = models.ForeignKey(TrailerOptions, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False })  # does the boat have a trailer?
	boat_location = models.CharField(max_length=20)  # Postcode where the boat is stored.
	travel_distance = models.PositiveSmallIntegerField(blank=True)  # estimated travel distance to the boat
	additional_info = HTMLField(blank=True, null=True)  # anything extra that might be needed about the boat.

	# consent
	my_consent = models.BooleanField(default=False)  # a record of the user's consent to be contacted.

	# admin fields
	is_approved = models.BooleanField(default=False)  # set to true if the quote has been approved
	approved_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, limit_choices_to={ 'is_staff' : True })  # who approved the quote?
	date_approved = models.DateTimeField(blank=True, null=True)  # date/time the quote was approved.

	# quote totals
	all_inclusive_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	scrap_only_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
	all_inclusive_monthly = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	scrap_only_monthly = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	# last updated
	updated = models.DateTimeField(auto_now=True)  # date and time of the last update made to the quote.

	# payment record
	is_paid = models.BooleanField(default=False)  # record that the quote has been paid.
	payment_type = models.CharField(max_length=1, blank=True, null=True, choices=PAYMENT_MADE_OPTIONS)  # records the job type.
	payment_id = models.CharField(max_length=50, blank=True)  # record of the payment id returned from stripe.
	date_paid = models.DateTimeField(blank=True, null=True)  # the date the payment was made.

	# quote declined by user.
	is_declined = models.BooleanField(default=False)  # a record that the user has declined the quote
	date_declined = models.DateTimeField(blank=True, null=True)  # the date the quote was declined

	def __unicode__(self):
		return "{0}ft - {1}".format(self.boat_length, self.type_of_boat)

	# class meta for the admin screen
	class Meta:
		verbose_name = 'Quote'
		verbose_name_plural = 'Quotes'


def user_upload_path(instance, filename):
		return 'user_{0}/{1}'.format(instance.user.id, filename)


# Model to hold uploaded images by the user relating to the quote.
class QuoteImages(models.Model):

	# fields.
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="quote_images")  # user who uploaded the image
	quote = models.ForeignKey(Quote, related_name="quote_images")  # quote the image belongs to
	file_path = models.ImageField(upload_to=user_upload_path)  # file path to the image
	created_at = models.DateTimeField(auto_now_add=True) # The day they uploaded it.

	# return the path.
	def __unicode__(self):
		return self.file_path


# Model to hold the QuoteLog Status Updates
class QuoteLogStatus(models.Model):

	# fields
	status = models.CharField(max_length=50)
	comment = models.CharField(max_length=150)
	is_disabled = models.BooleanField(default=False)

	# return status
	def __unicode__(self):
		return self.status

	# class meta for the admin screen
	class Meta:
		verbose_name = 'Quote Log Status Code'
		verbose_name_plural = 'Quote Log Status Codes'


# Model to hold the tracking log for the quote.
class QuoteLog(models.Model):

	# fields
	created_at = models.DateTimeField(auto_now_add=True)
	quote = models.ForeignKey(Quote, related_name="quote_logs")
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True, related_name="quote_logs")
	status = models.ForeignKey(QuoteLogStatus, on_delete=models.PROTECT, limit_choices_to={ 'is_disabled' : False }, related_name="quote_logs")
	comment = HTMLField(blank=True, null=True)
	ip_address = models.GenericIPAddressField(protocol='IPv4')

	# return status
	def __unicode__(self):
		return self.status.status


# save image details to database after it's been uploaded
@receiver(file_uploaded, sender=AjaxFileUploader)
def create_on_upload(sender, backend, request, **kwargs):
	# get the quote_id from the request and lookup the relevant quote.
	quoteID = Quote.objects.get(pk=request.GET.get('quote_id'))
	statusID = QuoteLogStatus.objects.get(pk=4)

	# find the start of the media upload directory in the path string.
	startIndex = backend.path.find(settings.MEDIA_URL)
	filePath = backend.path[startIndex::]

	# create the image record.
	QuoteImages.objects.create(user=request.user, quote=quoteID, file_path=filePath)

	# create the log entry.
	QuoteLog.objects.create(user=request.user, quote=quoteID, status=statusID, ip_address=request.META['REMOTE_ADDR'])
