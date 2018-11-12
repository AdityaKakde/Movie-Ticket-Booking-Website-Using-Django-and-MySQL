from django.forms import ModelForm
from django import forms

from .models import *

class signupform(ModelForm):

    class Meta:
        model = Customer
        fields = ['cus_name','cus_contact','username','password']

class loginform(forms.Form):
        username = forms.CharField()
        password = forms.CharField()

class eventform(ModelForm):

    class Meta:
        model = Event
        fields = [ 'event_name','event_time','date']
