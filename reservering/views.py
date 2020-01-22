from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer, Stylist


def index(request):
    return render(request, 'pages/index.html')


def appointment(request):
    allStylist = Stylist.objects.all()
    context = {'allStylist': allStylist}

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
