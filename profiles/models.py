from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib.staticfiles.templatetags.staticfiles import static

# Create your models here.


class Item(models.Model):
	owner = models.ForeignKey(User, related_name= 'items')
	item_name = models.CharField(max_length = 255)
	description = models.CharField(max_length = 255)
	price = models.IntegerField(default = 0);
	picture = models.FileField()
	when_created = models.DateTimeField(auto_now_add = True)

	
	def __str__(self):
		return '{} owned by: {}'.format(self.item_name, self.owner.username)

class ProfileStatus(models.Model):
	owner = models.OneToOneField(User, related_name="profile")
	money = models.IntegerField(default = 0)

	def __str__(self):
		return self.owner.username

class BidItem(models.Model):
	bidded_item = models.ForeignKey(Item, related_name="itembid")
	owner_bid = models.ForeignKey(User, related_name="bidowned")
	bid_cost = models.IntegerField(default=0)

	def __str__(self):
		return "{} : {}".format(self.bidded_item.item_name, self.bid_cost)