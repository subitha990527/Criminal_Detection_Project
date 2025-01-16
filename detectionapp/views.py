from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

# Create your views here.
from detectionapp.forms import PoliceRegister, LoginForm, CriminalRegister, MissingPersons, ComplaintMessage, \
    PublicRegister
from detectionapp.models import Policereg, Criminalreg, Addmissing, Complaint, Publicreg


def home(request):
    return render(request, "index.html")


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('adminpage')
            elif user.is_public:
                print(user)
                return redirect('public_page')
            elif user.is_police:
                return redirect('policepage')
                print(user)
            else:
                messages.info(request, 'Invalid Credentials')
    return render(request, "login.html")

#logout

def logout_view(request):
    logout(request)
    return redirect('loginpage')

















