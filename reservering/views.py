from django.shortcuts import render
from .forms import CustomerForm, DateForm
from .models import Customer, Stylist, Treatment, TreatmentOptions

from django.db.models import prefetch_related_objects


def index(request):
    return render(request, 'pages/index.html')


def appointment(request):
    allStylist = Stylist.objects.all()
    allTreatment = Treatment.objects.all()
    allTreatmentOptions = TreatmentOptions.objects.all()

    form = DateForm(request.POST or None)

    context = {'allStylist': allStylist,
               'allTreatment': allTreatment,
               'allTreatmentOptions': allTreatmentOptions,
               'form': form,
               }
    return render(request, 'pages/appointment.html', context)


def bevestiging(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        phone = form.cleaned_data['phone']
        e_mail = form.cleaned_data['e_mail']
        c = Customer(firstname=firstname, lastname=lastname, phone=phone, e_mail=e_mail)
        c.save()
    context = {'form': form}
    return render(request, 'pages/bevestiging.html', context)

def showcustomer(request):
    allCustomer = Customer.objects.all()
    context = {'allCustomer': allCustomer}

    return render(request, 'pages/klantgegevens.html', context)


from django.views import generic
