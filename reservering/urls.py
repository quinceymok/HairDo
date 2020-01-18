from django.urls import path
from . import views
#from . views import customer_list_view

urlpatterns = [
    path('', views.index, name='index'),
    path('appointment', views.appointment, name='appointment'),
    path('bevestiging', views.bevestiging, name='bevestiging'),
    path('klantgegevens', views.showcustomer, name= 'klantgegevens'),
    #path('klantgegevens', customer_list_view, name= 'klantgegevens'),

]




