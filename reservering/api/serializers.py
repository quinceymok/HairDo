from rest_framework import serializers
from reservering.models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'url','firstname', 'lastname', 'phone', 'e_mail', 'gender')

