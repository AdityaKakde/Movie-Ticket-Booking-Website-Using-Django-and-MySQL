from .models import Customer
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ValidationError

class CustomerBackend:

    def authenticate(request,username=None,password=None):
        try:
            user = Customer.objects.get(username=username)
            raise ValidationError(user)
        except Customer.DoesNotExist:
            raise ValidationError("Customer DoesNotExist")
            return None
        if user:
            print(user)
            password = Customer.objects.get(password=password)
            if password:
                return user
        return None

    def get_user(self,user_id):
        try:
            return Customer.objects.get(pk=user_id)
        except Customer.DoesNotExist:
            return None
