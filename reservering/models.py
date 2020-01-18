# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Availability(models.Model):
    date_id = models.ForeignKey('TimeSlot', blank=True, null=False, on_delete=models.PROTECT)  # Field name made lowercase.
    stylist_id = models.ForeignKey('Stylist', blank=True, null=False, on_delete=models.PROTECT)  # Field name made lowercase.
    available = models.SmallIntegerField(db_column='Available', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Availability'
        unique_together = (('date_id', 'stylist_id'),)


class ChosenTreatment(models.Model):
    appointment_id = models.ForeignKey('Appointment', blank=True, null=False, on_delete=models.PROTECT)  # Field name made lowercase.
    treatment_options_id = models.ForeignKey('TreatmentOptions', blank=True, null=False, on_delete=models.PROTECT)  # Field name made lowercase.

    class Meta:
        db_table = 'Chosen_Treatment'
        unique_together = (('appointment_id', 'treatment_options_id'),)


class Customer(models.Model):
    customer_id = models.AutoField(db_column='Customer_ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='Phone', max_length=10, blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E-mail', max_length=50, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    gender = models.CharField(db_column='Gender', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Customer'


class Stylist(models.Model):
    stylist_id = models.AutoField(db_column='Stylist_ID', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='Firstname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Stylist'


class TimeSlot(models.Model):
    date_id = models.AutoField(db_column='Date_ID', primary_key=True)  # Field name made lowercase.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Time_slot'


class Treatment(models.Model):
    treatment_id = models.AutoField(db_column='Treatment_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Treatment'


class TreatmentOptions(models.Model):
    treatment_options_id = models.AutoField(db_column='Treatment_Options_ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, blank=True, null=True)  # Field name made lowercase.
    treatment_id = models.ForeignKey('Treatment', blank=True, null=False, on_delete=models.PROTECT)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Treatment_Options'


class Appointment(models.Model):
    appointment_id = models.AutoField(db_column='Appointment_ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.ForeignKey('Customer', on_delete=models.PROTECT)  # Field name made lowercase.
    stylist_id = models.ForeignKey('Stylist', on_delete=models.PROTECT)  # Field name made lowercase.
    date_id = models.ForeignKey('TimeSlot', on_delete=models.PROTECT)  # Field name made lowercase.

    class Meta:
        db_table = 'Appointment'

