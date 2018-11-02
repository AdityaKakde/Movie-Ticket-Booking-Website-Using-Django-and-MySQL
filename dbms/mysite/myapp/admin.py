from django.contrib import admin
from .models import Event,Login,Payment,Stats,Views,Manager,Customer

# Register your models here.

admin.site.register(Event)
admin.site.register(Login)
admin.site.register(Payment)
admin.site.register(Stats)
admin.site.register(Views)
admin.site.register(Customer)
