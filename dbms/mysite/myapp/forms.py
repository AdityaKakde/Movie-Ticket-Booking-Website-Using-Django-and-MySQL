from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
    get_user_model,
    )
# from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import login as log

User = get_user_model()

class signupform(ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput,label='CONFIRM PASSWORD')

    class Meta:
        model = Customer
        fields = ['cus_name','cus_contact','username','password']
        # initial_fields = ['John Doe']
        labels ={
            'cus_name': ('NAME'),
            'cus_contact': ('EMAIL'),
            'username': ('USERNAME'),
            'password': ('PASSWORD'),
        }
        widgets = {
            'password2':forms.PasswordInput(),
            'cus_name':forms.TextInput(attrs={'placeholder':"John Doe"}),
            'password':forms.PasswordInput(),
            'cus_contact': forms.EmailInput(attrs={'placeholder':'john@gmail.com'}),
            'username':forms.TextInput(attrs={'placeholder':"john"})

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
            # return redirect(signupform)

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
        username =  forms.CharField(label='USERNAME')
        email = forms.EmailField(label='EMAIL')
        email2 = forms.EmailField(label='CONFIRM EMAIL')
        password =  forms.CharField(widget=forms.PasswordInput,label='PASSWORD')

        class Meta:
            model = User
            fields = {
                'username',
                'password',
                'email2',
                'email',

                }

        def clean_email2(self):
            email= self.cleaned_data.get('email')
            email2= self.cleaned_data.get('email2')
            password= self.cleaned_data.get('password')
            if email!=email2:
                raise forms.ValidationError("Emails must match")
            email_qs = User.objects.filter(username=username)
            if email_qs.exists():
                raise forms.ValidationError("Email already registred")


            return super(ManagerRegistrationForm,self).clean(*args,**kwargs)

class loginform(forms.Form):
        username = forms.CharField(label='USERNAME')
        password = forms.CharField(widget=forms.PasswordInput,label='PASSWORD')


        def clean(self):
            username= self.cleaned_data.get('username')
            password= self.cleaned_data.get('password')
            userz=Customer.objects.all()
            print(userz)
            print('f1')
            user= authenticate(username=username,password=password)
            print('f2')
            print(user)
            if username and password:
                if not user:
                     print('Form Not user')
                     raise forms.ValidationError("User nonexistent")
                if not user.check_password(password):
                     print('Form pw incorrect')
                     raise forms.ValidationError("Incorrect password")
            return super(loginform,self).clean()
            # user_qs= Customer.objects.filter(username=username)
            # print(user_qs)
            # print('username exists')
            # if user_qs.exists():
            #     pass_qs= user_qs.password
            #     print(pass_qs)
            #     print('password exists')
            #     if password!=pass_qs:
            #         print('password exists')
            #         raise forms.ValidationError("Wrong username or password")

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
            'event_time':forms.TimeInput(attrs={'placeholder':""}),
            'event_name':forms.TextInput(attrs={'placeholder':""}),

        }

        def clean():
            event_name = form.cleaned_data.get(event_name)
            event_time = form.cleaned_data.get(event_time)
            date = form.cleaned_data.get(date)

            name_qs=Event.objects.filter(event_name=event_name)
            if name_qs.exists():
                raise forms.ValidationError('Enter valid name')
