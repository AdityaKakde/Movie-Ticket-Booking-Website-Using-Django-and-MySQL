# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Admin(models.Model):
    username = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admin'


class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=10, blank=True, null=True)
    event_time = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'booking'


class Customer(models.Model):
    cus_id = models.AutoField(primary_key=True)
    cus_name = models.CharField(max_length=20, blank=True, null=True)
    cus_contact = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=10, blank=True, null=True)
    password = models.CharField(max_length=10, blank=True, null=True)


    def __str__(self):
        return self.cus_name

    class Meta:
        managed = False
        db_table = 'customer'



class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=10, blank=True, null=True)
    event_time = models.CharField(max_length=10, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.event_name

    class Meta:
        managed = False
        db_table = 'event'


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    pay_amt = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    event = models.ForeignKey(Event, models.DO_NOTHING, blank=True, null=True)
    cus = models.ForeignKey(Customer, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment'
