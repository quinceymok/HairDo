from rest_framework import serializers
from reservering.models import Customer, Stylist, Treatment, TimeSlot


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

