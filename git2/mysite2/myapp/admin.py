from django.contrib import admin
from myapp.models import Customer,Event,Payment,Booking,Admin
# Register your models here.

admin.site.register(Customer)
admin.site.register(Event)
admin.site.register(Payment)
admin.site.register(Booking)
admin.site.register(Admin)
