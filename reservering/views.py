from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer


def index(request):
    return render(request, 'pages/index.html')


def appointment(request):
    return render(request, 'pages/appointment.html')


def bevestiging(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        first_name = form.cleaned_data['first_name']
        last_name = form.cleaned_data['last_name']
        phone_number = form.cleaned_data['phone_number']
        email = form.cleaned_data['email']
        c = Customer(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email)
        c.save()
    context = {'form': form}
    return render(request, 'pages/bevestiging.html', context)
