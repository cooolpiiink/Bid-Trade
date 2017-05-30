from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse
from profiles.models import Item,ProfileStatus

def home(request):
	context={
		'items':Item.objects.all().order_by('-when_created')
	}
	return render(request, 'home.html', context = context)

def detail(request, item_id):
	item = get_object_or_404(Item, pk =item_id)
	context = {
		'item': item
	}
	return render(request, 'detail.html', context = context)