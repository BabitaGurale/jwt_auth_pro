from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    GENDER =[('male','male'),('female',"female"),('other',"other")]
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=20,choices=GENDER)
    address = models.TextField(max_length=20)
    city = models.CharField(max_length=20)
    contact_no = PhoneNumberField(region="IN")
    aadhar_card_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
