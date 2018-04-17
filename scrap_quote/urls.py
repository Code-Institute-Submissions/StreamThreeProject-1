from django.conf.urls import url

import views

urlpatterns = [

	# create/edit quotations.
	url(r'^new/$', views.new_quotation, name="new_quote"),  # new quote.
	url(r'^edit/(?P<quote_id>\d+)/$', views.edit_quotation, name="edit_quote"),  # edit quotation.
	url(r'^approve/(?P<quote_id>\d+)/$', views.approve_quotation, name="approve_quote"),  # approve quotation.
	url(r'^decline/(?P<quote_id>\d+)/$', views.decline_quotation, name="decline_quote"),  # decline quotation.
	url(r'^pay/(?P<quote_id>\d+)/(?P<payment_type>all|disposal)/$', views.pay_quotation, name="pay_quote"),  # pay the quote.

	# view quotation.
	url(r'^view/(?P<quote_id>\d+)/$', views.view_quotation, name="view_quote"),  # view quotation.
	url(r'^activity_log/(?P<quote_id>\d+)/$', views.quote_activity_log, name="activity_log"),  # quotation activity log.
	url(r'^activity_log/new/(?P<quote_id>\d+)$', views.add_quote_activity, name="add_activity"),  # add a new activity to the log.

	# ajax image uploader.
	url(r'ajax-upload$', views.import_uploader, name="quote_image_ajax"),  # used to upload images via ajax.
]