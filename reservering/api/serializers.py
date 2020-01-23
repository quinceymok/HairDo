from rest_framework import serializers
from reservering.models import (
    Customer, Stylist, Treatment, TimeSlot, TreatmentOptions, ChosenTreatment, Appointment)


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'url','firstname', 'lastname', 'phone', 'e_mail', 'gender')


class StylistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Stylist
        fields = ('stylist_id', 'url', 'firstname', 'lastname')


class TreatmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Treatment
        fields = ('treatment_id', 'url', 'name')


class TimeSlotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ('date_id', 'url', 'date')


class TreatmentOptionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TreatmentOptions
        fields = ('treatment_options_id', 'url', 'name', 'treatment_id', 'duration')


class ChosenTreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChosenTreatment
        fields = ('appointment_id', 'treatment_options_id', 'url')


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Appointment
        fields = ('appointment_id', 'customer_id', 'stylist_id', 'date_id', 'url')

