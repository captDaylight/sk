from django.db import models
from django import forms

class SignupForm(forms.Form):
	username = forms.CharField(max_length = 100)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(render_value=False),max_length=100)
	