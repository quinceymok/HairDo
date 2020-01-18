from django.contrib import admin
from .models import Customer, Stylist, Appointment, TimeSlot, Treatment, TreatmentOptions, Availability, ChosenTreatment


# Register your models here.
admin.site.register(Customer)
admin.site.register(Stylist)
admin.site.register(Appointment)
admin.site.register(TimeSlot)
admin.site.register(Treatment)
admin.site.register(TreatmentOptions)
admin.site.register(Availability)
admin.site.register(ChosenTreatment)

