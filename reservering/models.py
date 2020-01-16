from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.phone_number + ' ' + self.email

#create primary keys.
class Stylist(models.Model):
    stylist_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


