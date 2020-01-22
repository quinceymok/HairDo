from django.shortcuts import render
from rest_framework import viewsets
from reservering.models import Customer, Stylist, Treatment, TimeSlot
from .serializers import CustomerSerializer, StylistSerializer, TreatmentSerializer, TimeSlotSerializer


class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class StylistView(viewsets.ModelViewSet):
    queryset = Stylist.objects.all()
    serializer_class = StylistSerializer

class TreatmentView(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer

class TimeSlotView(viewsets.ModelViewSet):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer
