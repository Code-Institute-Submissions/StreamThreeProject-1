from django import forms
from django.core.exceptions import ValidationError

from .models import Quote, QuoteImages
import math


# form to create/edit scrap quotations
class QuotationForm(forms.ModelForm):

	# add 'form-control' class to all fields on the form.
	def __init__(self, *args, **kwargs):
		super(forms.ModelForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


	LENGTH_CHOICES = (
		('feet', 'Feet'),
		('metres', 'Metres')
	)

	WEIGHT_CHOICES = (
		('tonnes', 'Tonnes'),
		('kilograms', 'Kilograms')
	)

	length_type = forms.ChoiceField(choices=LENGTH_CHOICES, required=True, initial='feet')
	weight_type = forms.ChoiceField(choices=WEIGHT_CHOICES, required=True, initial='tonnes')

	class Meta:
		
		model = Quote
		fields = '__all__'
		exclude = [ 'approved_by', 'date_approved', 'all_inclusive_total', 
					'all_inclusive_monthly', 'scrap_only_total', 'scrap_only_monthly',
					'ip_address', 'travel_distance'
				  ]

	
	# calculate the boat length
	def clean_boat_length(self):
		
		# get the form data.
		_length = self.cleaned_data.get('boat_length')
		_type = self.data['length_type']

		# if feet has been selected.
		if _type == 'feet':

			# return the length
			return _length
		
		# if metres has been selected.
		else:
			
			# return the ceiling of length multiplied by 3.3
			return math.ceil(_length * 3.3)


	# calculate the weight of the boat
	def clean_boat_weight(self):

		# get the form data.
		_weight = self.cleaned_data.get('boat_weight')
		_type = self.data['weight_type']

		# if tonnes is selected.
		if _type == 'tonnes':

			# return the weight
			return _weight

		# if kilograms is selected
		else:

			# return the ceiling of weight divided by 1000
			return math.ceil(_weight / 1000)


# form to pay for a quote.
class PayForQuoteForm(forms.Form):

	# add 'form-control' class to all fields on the form.
	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


	MONTH_ABBREVIATIONS = [
		'Jan', 'Feb', 'Mar', 'Apr', 'May', 'June',
		'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec'
	]
	MONTH_CHOICES = list(enumerate(MONTH_ABBREVIATIONS, 1))
	YEAR_CHOICES = [(i, i) for i in range(2018, 2036)]

	credit_card_number = forms.CharField(label="Credit Card Number")
	cvv = forms.CharField(label="Security Code (CVV)")
	expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES)
	expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES)
	payment_id = forms.CharField(widget=forms.HiddenInput)


	class Meta:
		fields = ['credit_card_number', 'cvv', 'expiry_month', 'expiry_year', 'payment_id']
