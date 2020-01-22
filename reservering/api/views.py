from django.shortcuts import render
from rest_framework import viewsets
from reservering.models import Customer, Stylist, Treatment, TimeSlot, TreatmentOptions, ChosenTreatment, Availability, Appointment
from .serializers import (
    CustomerSerializer, StylistSerializer, TreatmentSerializer, TimeSlotSerializer, TreatmentOptionsSerializer,
    ChosenTreatmentSerializer, AvailabilitySerializer, AppointmentSerializer
)


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


class TreatmentOptionsView(viewsets.ModelViewSet):
    queryset = TreatmentOptions.objects.all()
    serializer_class = TreatmentOptionsSerializer


class ChosenTreatmentView(viewsets.ModelViewSet):
    queryset = ChosenTreatment.objects.all()
    serializer_class = ChosenTreatmentSerializer

class AvailabilityView(viewsets.ModelViewSet):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

class AppointmentView(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
