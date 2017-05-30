# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from profiles.forms import RegistrationForm
from django.urls import reverse
from .forms import UserInfoForm
from .models import Item,ProfileStatus,BidItem
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)

        if user:
            login(request, user)
            return redirect('/')
        else:
            context['error'] = 'Invalid username of password'
            context['username'] = username
    
    return render(request, 'profiles/registration/login.html', context = context)

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    context = {}
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = RegistrationForm()
    context['form'] = form
    return render(request, 'profiles/registration/signup.html',context = context)

def sign_out(request):
    logout(request)
    return redirect('sign_in')

class ItemCreate(CreateView):
    model = Item
    fields = ['owner','item_name', 'description', 'price','picture']

    def get_initial(self):
        return {'owner': self.request.user }

def add_money(request):
    if not request.user.is_authenticated:
        return redirect('sign_in')

    if request.method == 'POST':
        form = UserInfoForm(request.POST,instance=request.user)
        money = request.POST.get('money')

        temp = ProfileStatus.objects.filter(owner = request.user)
        if temp is None:
            ProfileStatus.objects.create(owner= request.user, money = money )
        else:
            ProfileStatus.objects.update(owner = request.user, money = money)
        return redirect('/')
    else:
        form = UserInfoForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'profiles/add_money.html', context=context)


def addbid(request):
    if not request.user.is_authenticated:
        return redirect(reverse('sign_in'))
    if request.method == "POST":
        cost = request.POST.get('bid_cost')
        b_id = request.POST.get('itempk')
        b_itemname = request.POST.get('itemname')
        item = Item.objects.get(pk = b_id)
        BidItem.objects.create(bidded_item = item, owner_bid = request.user, bid_cost= cost)
    return redirect('/')




