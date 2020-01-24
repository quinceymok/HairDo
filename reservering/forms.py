from django.forms import ModelForm
from .models import Customer
from django import forms


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname', 'lastname', 'phone', 'e_mail']


class DateInput(forms.DateInput):
    input_type = 'date'


class DateForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput())

