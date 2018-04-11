from django.conf.urls import url

import views

urlpatterns = [

	# create/edit quotations
	url(r'^new/$', views.new_quotation, name="new_quote"),  # new quote
	url(r'^edit/(?P<quote_id>\d+)/$', views.edit_quotation, name="edit_quote"),  # edit quotation

	# view quotation
	url(r'^view/(?P<quote_id>\d+)/$', views.view_quotation, name="view_quote"),  # view quotation
]