from django.contrib import admin
from .models import Customer, Stylist, Appointment, TimeSlot, Treatment, TreatmentOptions, Availability, ChosenTreatment


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'firstname', 'lastname', 'phone', 'e_mail', 'gender')
admin.site.register(Customer,CustomerAdmin)

class StylistAdmin(admin.ModelAdmin):
    list_display = ('stylist_id', 'firstname', 'lastname')
admin.site.register(Stylist, StylistAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'customer_id', 'stylist_id', 'date_id')
admin.site.register(Appointment, AppointmentAdmin)

class TimeSlotAdmin(admin.ModelAdmin):
    list_display = ('date_id', 'date')
admin.site.register(TimeSlot, TimeSlotAdmin)

class TreatmentAdmin(admin.ModelAdmin):
    list_display = ('treatment_id', 'name')
admin.site.register(Treatment, TreatmentAdmin)

class TreatmentOptionsAdmin(admin.ModelAdmin):
    list_display = ('treatment_options_id', 'name', 'treatment_id', 'duration')
admin.site.register(TreatmentOptions, TreatmentOptionsAdmin)

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = ('date_id', 'stylist_id', 'available')
admin.site.register(Availability, AvailabilityAdmin)

class ChosenTreatmentAdmin(admin.ModelAdmin):
    list_display = ('appointment_id', 'treatment_options_id')
admin.site.register(ChosenTreatment, ChosenTreatmentAdmin)

