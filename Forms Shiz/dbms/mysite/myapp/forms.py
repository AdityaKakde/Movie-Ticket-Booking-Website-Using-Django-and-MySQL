from django.forms import ModelForm
from django import forms

from .models import Event,Admin,Payment,Customer,Booking

class signupform(ModelForm):

    class Meta:
        model = Customer
        fields = ['cus_name','cus_contact','username','password']

class loginform(forms.Form):
        username = forms.CharField()
        password = forms.CharField()

# from django import forms
#
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)
