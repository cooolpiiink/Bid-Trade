
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import  Item,ProfileStatus,BidItem

class ProfileAdmin(admin.ModelAdmin):
	search_fields = ['owner__username']

admin.site.register(ProfileStatus, ProfileAdmin)
admin.site.register(Item)
admin.site.register(BidItem)