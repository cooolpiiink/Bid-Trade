from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Item,ProfileStatus


class RegistrationForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2'
		)
	def save(self, commit = True):
		user = super(RegistrationForm, self).save(commit = False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class UserInfoForm(forms.ModelForm):
	money = forms.IntegerField(required=False)

	def save(self, commit=True):
		instance = super(UserInfoForm, self).save(commit=commit)
		if self.cleaned_data['money']:
			instance.money = self.cleaned_data['money']
			instance.save()
	
	class Meta:
		model = User
		fields = ['username','money']