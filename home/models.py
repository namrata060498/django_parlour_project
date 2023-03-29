from django.db import models


class Client_Feedback(models.Model):
    clientname = models.CharField(max_length=40)
    clientfeedback=models.CharField(max_length=120)
    clientage = models.IntegerField()
    email = models.EmailField()
    contactno = models.IntegerField()

    class Meta:
        db_table = "Client"

class Book_Appointment(models.Model):
    Client_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Contact_Number = models.IntegerField()
    Appointment_Date = models.DateField()
    Appointment_Time = models.TimeField()

    class Meta:
        db_table = "BookAppointment"





# Create your models here.
