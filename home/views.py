from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from home.forms import SignUpForm, Client_F, Client_B
from home.models import Book_Appointment, Client_Feedback


def signin(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                return render(request, 'home.html')
    else:
        fm = AuthenticationForm()

    return render(request, 'signin.html',{'form': fm})


def signup(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'signup.html')
    else:
        fm = SignUpForm()
        return render(request,'signup.html',{'form': fm})


def logout(request):
    return render(request,'profile.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def feedback(request):
    if request.method == "POST":
        fm = Client_F(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Client_F()
    return render(request, 'feedback.html', {'form': fm})


def wax(request):
    return render(request,'wax.html')

def facial(request):
    return render(request,'facial.html')

def cleanup(request):
    return render(request,'cleanup.html')

def hairspa(request):
    return render(request,'haircut.html')

def gallery(request):
    return render(request,'gallery.html')

def appointment(request):
    if request.method == "POST":
        fm = Client_B(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = Client_B()
    return render(request, 'appointment.html', {'form': fm})

def showdetail(request):
    clientdetail=Book_Appointment.objects.all()
    return render(request,"show_appointment.html",{"client":clientdetail})

def showfeedback(request):
    clientfeedback=Client_Feedback.objects.all()
    return render(request,"show_feedback.html",{"feedback":clientfeedback})

# Create your views here.
