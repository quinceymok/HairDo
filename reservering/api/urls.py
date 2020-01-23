from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('customer', views.CustomerView)
router.register('stylist', views.StylistView)
router.register('treatment', views.TreatmentView)
router.register('timeslot', views.TimeSlotView)
router.register('treatmentoptions', views.TreatmentOptionsView)
router.register('chosentreatment', views.ChosenTreatmentView)
router.register('appointment', views.AppointmentView)

urlpatterns = [
    path('', include(router.urls))
]

