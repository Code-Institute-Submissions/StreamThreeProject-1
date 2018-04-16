# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.db import models
from django import forms

from .models import *


admin.site.disable_action('delete_selected')

# Model Admin for Quotes.
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
	list_display = ('user', 'created_at', 'type_of_boat', 'boat_length', 'boat_weight', 'all_inclusive_total')
	date_hierarchy = 'created_at'
	search_fields = ['user_id__email', 'user_id__first_name', 'user_id__last_name', 
					 'user_id__post_code', 'type_of_boat_id__type_of_boat']
	fieldsets = (
		('Quote Created By', {
			'fields' : ('user',),
			}),
		('Boats Details', {
			'fields' : ('type_of_boat', 'keel_type', 'boat_length', 'boat_weight', 'hull_material', 'hazardous_mats')
			}),
		('Engine Details', {
			'fields' : ('engine', 'engine_make', 'engine_cylinders', 'engine_hours', 'engine_still_run')
			}),
		('Location Details', {
			'fields' : ('scrap_at_location', 'boat_in_water', 'has_trailer', 'boat_location', 'travel_distance')
			}),
		('Additional Information', {
			'fields' : ('my_consent', 'additional_info',)
			}),
		('Prices', {
			'fields' : ('all_inclusive_total', 'all_inclusive_monthly', 'scrap_only_total', 'scrap_only_monthly')
			}),
		('Quote Approval', {
			'classes' : ('collapse',),
			'fields' : ('is_approved', 'approved_by', 'date_approved')
			}),
		('Payment Options', {
			'classes' : ('collapse',),
			'fields' : ('is_paid', 'payment_type', 'date_paid', 'payment_id')
			}),
		('Quote Declined', {
			'classes' : ('collapse',),
			'fields' : ('is_declined', 'date_declined')
			}),
	)


# Model Admin for Hazardous Materials
@admin.register(HazardousMaterials)
class HazardousMatsAdmin(admin.ModelAdmin):
	list_display = ('mat_type', 'cost', 'is_disabled')


# Model Admin for Type of Boat
@admin.register(TypeOfBoat)
class TypeOfBoatAdmin(admin.ModelAdmin):
	list_display = ('type_of_boat', 'cost', 'is_disabled')


# Model Admin for Type of Keel
@admin.register(TypeOfKeel)
class TypeOfKeelAdmin(admin.ModelAdmin):
	list_display = ('type_of_keel', 'cost', 'is_disabled')


# Model Admin for Hull Material
@admin.register(HullMaterials)
class HullMaterialAdmin(admin.ModelAdmin):
	list_display = ('hull_material', 'cost', 'is_disabled')


# Model Admin for Engine Types
@admin.register(EngineTypes)
class EngineTypesAdmin(admin.ModelAdmin):
	list_display = ('engine_type', 'cost', 'is_disabled')


# Model Admin for Engine Still Runs
@admin.register(EngineStillRun)
class EngineStillRunAdmin(admin.ModelAdmin):
	list_display = ('engine_still_run', 'is_disabled')


# Model Admin for Trailer Options
@admin.register(TrailerOptions)
class TrailerOptionsAdmin(admin.ModelAdmin):
	list_display = ('trailer_option', 'cost', 'is_disabled')


# Model Admin for Boat in the Water Options
@admin.register(BoatInWaterOptions)
class BoatInWaterOptionsAdmin(admin.ModelAdmin):
	list_display = ('is_in_water', 'cost', 'is_disabled')


# Model Admin for Scrap at Location
@admin.register(ScrapAtLocation)
class ScrapAtLocationAdmin(admin.ModelAdmin):
	list_display = ('scrap_at_location', 'cost', 'is_disabled')


# Model Admin for QuoteLogStatus
@admin.register(QuoteLogStatus)
class QuoteLogStatusAdmin(admin.ModelAdmin):
	list_display = ('pk', 'status', 'comment', 'is_disabled')
	list_display_links = ('pk', 'status')
