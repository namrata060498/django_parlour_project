from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from home.models import Client_Feedback, Book_Appointment


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password1','password2']

class Client_F(forms.ModelForm):
    class Meta:
        model=Client_Feedback
        fields = ['clientname', 'clientfeedback', 'clientage', 'email', 'contactno']

class Client_B(forms.ModelForm):
    class Meta:
        model=Book_Appointment
        fields = ['Client_Name', 'Email', 'Contact_Number', 'Appointment_Date', 'Appointment_Time']