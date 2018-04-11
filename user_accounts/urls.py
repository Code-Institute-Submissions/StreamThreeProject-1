from django.conf.urls import url

import views as accounts

urlpatterns = [

	# user accounts
	url(r'^register/$', accounts.register, name='register'), # user registration
	url(r'^login/$', accounts.login, name='login'), # user log in
	url(r'^logout/$', accounts.logout, name='logout'), # user log out
	url(r'^$', accounts.my_account, name='my_account'), # my account home page

	# ajax calls
	url(r'^ajax/check_email/$', accounts.lookup_email, name='lookup_email') # check email address doesn't exist
]