from django.forms import ModelForm
from django import forms
from django.template import RequestContext
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import datetime
from django.contrib.auth import (
    authenticate,
    get_user_model,
    )
from .models import *
from django.contrib.auth import login as log

User = get_user_model()

class signupform(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput,label='CONFIRM PASSWORD')

    class Meta:
        model = Customer
        fields = ['cus_name','cus_contact','username','password']

        labels ={
            'cus_name': ('NAME'),
            'cus_contact': ('EMAIL'),
            'username': ('USERNAME'),
            'password': ('PASSWORD'),
        }
        widgets = {
            'password2':forms.PasswordInput(),
            'cus_name':forms.TextInput(attrs={'placeholder':"John Doe",'required':True}),
            'password':forms.PasswordInput(attrs={'required':True}),
            'cus_contact': forms.EmailInput(attrs={'placeholder':'john@gmail.com','required':True}),
            'username':forms.TextInput(attrs={'placeholder':"john",'required':True})

        }

    def clean_username(self):
            print(self.cleaned_data)
            username= self.cleaned_data.get('username')
            user_qs = Customer.objects.filter(username=username)
            print(user_qs)
            print("username")
            if user_qs.exists():
                raise forms.ValidationError("User already exists")
            return username
            #return redirect(signupform)

    def clean_cus_contact(self):
        print(self.cleaned_data)
        cus_contact= self.cleaned_data.get('cus_contact')
        email_qs = Customer.objects.filter(cus_contact=cus_contact)
        print(email_qs)
        if email_qs.exists():
            print (email_qs )
            print ("email")
            raise forms.ValidationError("Email already registred")
        return cus_contact
        # return redirect(signupform)
    def clean_password2(self):

        password= self.cleaned_data.get('password')
        password2= self.cleaned_data.get('password2')
        if password!=password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
# return redirect(signupform)


class UserLoginForm(forms.Form):
        username = forms.CharField(label='USERNAME')
        password = forms.CharField(widget=forms.PasswordInput,label='PASSWORD')

        def clean(self):
            username= self.cleaned_data.get('username')
            password= self.cleaned_data.get('password')

            if username and password:
                user = authenticate(username=username, password=password)
                if not user:
                     print('Form Not user')
                     raise forms.ValidationError("User nonexistent")
                if not user.check_password(password):
                     print('Form pw incorrect')
                     raise forms.ValidationError("Incorrect password")
                # if not user.is_active(password):
                #     raise forms.ValidationError("Inactive User")
            return super(UserLoginForm, self).clean()

class ManagerRegistrationForm(ModelForm):


        username=forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)
        email = forms.EmailField(label='Email')
        email2 = forms.EmailField(label='Confirm Email')





        class Meta:
            model = User
            fields = {
                'username',
                'password',
                'email',
                'email2',








                }
        def clean_email2(self):
            username= self.cleaned_data.get('username')
            password= self.cleaned_data.get('password')
            email= self.cleaned_data.get('email')
            email2= self.cleaned_data.get('email2')


            if email!=email2:
                raise forms.ValidationError("Emails must match")
            email_qs = User.objects.filter(username=username)
            if email_qs.exists():
                raise forms.ValidationError("Email already registred")
            return super(ManagerRegistrationForm,self).clean()
                # labels ={
                #     'email': ('EMAIL'),
                #     'email2': ('CONFIRM EMAIL'),
                #     'username': ('USERNAME'),
                #     'password': ('PASSWORD'),
                # }
                # widgets = {
                #     'password2':forms.PasswordInput(),
                #     'email2':forms.TextInput(attrs={'placeholder':"abc@email.com",'required':True}),
                #     'password':forms.PasswordInput(attrs={'required':True}),
                #     'email':forms.TextInput(attrs={'placeholder':"abc@email.com",'required':True}),
                #     'username':forms.TextInput(attrs={'placeholder':"john",'required':True})
                #
                # }

class loginform(forms.Form):
        username = forms.CharField(label='USERNAME')
        password = forms.CharField(widget=forms.PasswordInput,label='PASSWORD')


        def clean(self):
            username= self.cleaned_data.get('username')
            password= self.cleaned_data.get('password')

            try:
                user = Customer.objects.get(username=username,password=password)
            except Customer.DoesNotExist:
                raise forms.ValidationError("Invalid Credentials")
            return super(loginform,self).clean()


class eventform(ModelForm):

    class Meta:
        model = Event
        fields = [ 'event_name','event_time','date']
        labels ={
            'event_name': ('EVENT NAME'),
            'event_time': ('EVENT TIME'),
            'date': ('DATE'),
        }
        widgets = {
            'event_time':forms.TimeInput(attrs={'required':True}),
            'event_name':forms.TextInput(attrs={'required':True}),
            'date':forms.DateInput(attrs={'required':True})
        }

        def clean(self):
            event_name = form.cleaned_data.get(event_name)
            event_time = form.cleaned_data.get(event_time)
            date = form.cleaned_data.get(date)

            name_qs=Event.objects.filter(event_name=event_name)
            print(name_qs)
            print("name_qs")
            if name_qs.exists():
                raise forms.ValidationError('Enter valid name')




        def clean_date(self):
            date = form.cleaned_data['date']
            if date < datetime.date.today():
                raise forms.ValidationError("The date cannot be in the past!")
            return date
