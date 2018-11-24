from django.contrib import admin
from .models import Event,Admin,Payment,Customer,Booking

# Register your models here.

admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Admin)
admin.site.register(Customer)
