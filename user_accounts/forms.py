from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

from .models import User


# create the User Creation Form
class UserRegistrationForm(UserCreationForm):

	# add 'form-control' class to all fields on the form.
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'


	# define the fields
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
	email = forms.EmailField(required=True, label='E-Mail Address')

	
	class Meta:
		model = User
		fields = [
			'title', 'first_name', 'last_name', 'email', 
			'telephone', 'post_code', 'address_line_1', 'address_line_2', 
			'address_town', 'address_city','address_county', 'password1', 'password2'
		]
		exclude = ['username']


	# check password and password confirm fields match
	def clean_password(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		# check passwords match
		if password1 and password2 and password1 != password2:
			message = "Your passwords do not match"
			raise ValidationError(message)

		# return the password
		return password2


	# check username doesn't already exist
	def clean_email(self):
		email = self.cleaned_data.get('email')

		if User.objects.filter(email__iexact=email).exists():
			message = "This e-mail address is already in use, please try another"
			raise ValidationError(message)

		# return the email address
		return email


	# override the default save function
	def save(self, commit=True):
		_user = super(UserRegistrationForm, self).save(commit=False)

		# set the username as the e-mail address
		_user.username = _user.email

		# if a commit, save the user to the database
		if commit:
			_user.save()

		# return the user
		return _user


# Login Form
class UserLoginForm(forms.Form):

	# add 'form-control' class to all fields on the form.
	def __init__(self, *args, **kwargs):
		super(forms.Form, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		fields = ['email', 'password']
