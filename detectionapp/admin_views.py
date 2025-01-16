from django.contrib import messages
from django.shortcuts import render, redirect

from detectionapp.forms import LoginForm, PoliceRegister, CriminalRegister, MissingPersons, Notification
from detectionapp.models import Policereg, Publicreg, Criminalreg, Addmissing, Complaint, Notify, Login


def adminpage(request):
    return render(request, "admintemp/admin.html")

#register police station

def registrationpage(request):
    user_form = LoginForm()
    police_form = PoliceRegister()
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        police_form = PoliceRegister(request.POST, request.FILES)
        if user_form.is_valid() and police_form.is_valid():
            user = user_form.save(commit=False)
            user.is_police = True
            user.save()
            police = police_form.save(commit=False)
            police.user = user
            police_form.save()
            messages.info(request, 'Registered Successfully')
            return redirect('adminpage')
    return render(request, 'admintemp/registration.html', {'user_form': user_form, 'police_form': police_form})



#view police station

def police_view1(request):
    data = Policereg.objects.all()
    return render(request, "admintemp/police_view1.html", {'data': data})


#remove police station

def removepolice(request, id):
    data = Policereg.objects.get(id=id)
    data.delete()
    return redirect('police_view1')


#update police station

def updatepolice(request, id):
    police = Policereg.objects.get(id=id)
    police_form = PoliceRegister(instance=police)
    if request.method == 'POST':
        police_form = PoliceRegister(request.POST,request.FILES, instance=police)
        if police_form.is_valid():
            police_form.save()
            return redirect('police_view1')
    return render(request, 'admintemp/policeupdate.html', {'police_form': police_form})


#public view


def public_view(request):
    publicdata = Publicreg.objects.all()
    return render(request, "admintemp/view_public.html", {'publicdata': publicdata})


#remove public

def removepublic(request,id=None):
    publicdata = Login.objects.filter(is_public = True)
    publicdata.delete()
    return redirect('public_view')

# add criminals or registration

def criminalregpage(request):
    criminal_form = CriminalRegister()
    if request.method == 'POST':
        criminal_form = CriminalRegister(request.POST, request.FILES)
        if criminal_form.is_valid():
            criminal_form.save()
            messages.info(request, 'Registered Successfully')
            return redirect('adminpage')
    return render(request, 'admintemp/criminalreg.html', {'criminal_form': criminal_form})

#view criminals details

def criminal_view(request):
    criminaldata = Criminalreg.objects.all()
    return render(request, "admintemp/criminal_view.html", {'criminaldata': criminaldata})

#remove criminals

def removecriminal(request, id):
    criminaldata = Criminalreg.objects.get(id=id)
    criminaldata.delete()
    return redirect('criminal_view')

#update crminals


def updatecriminal(request, id):
    criminal = Criminalreg.objects.get(id=id)
    criminal_form = CriminalRegister(instance=criminal)
    if request.method == 'POST':
        criminal_form = CriminalRegister(request.POST,request.FILES, instance=criminal)
        if criminal_form.is_valid():
            criminal_form.save()
            return redirect('criminal_view')
    return render(request, 'admintemp/criminalupdate.html', {'criminal_form': criminal_form})


#view missing persons

def missing_view2(request):
    missingdata = Addmissing.objects.all()
    return render(request, "admintemp/view_missing2.html", {'missingdata': missingdata})

#removemissingpersons

def removemissing1(request, id):
    missingdata = Addmissing.objects.get(id=id)
    missingdata.delete()
    return redirect('missing_view2')

#updatemissing persons

def updatemissing1(request, id):
    missing = Addmissing.objects.get(id=id)
    missing_form = MissingPersons(instance=missing)
    if request.method == 'POST':
        missing_form = MissingPersons(request.POST,request.FILES, instance=missing)
        if missing_form.is_valid():
            missing_form.save()
            return redirect('missing_view2')
    return render(request, 'admintemp/update_missing1.html', {'missing_form': missing_form})


#view public complaints

def complaint_view1(request):
    u = Complaint.objects.all()
    return render(request, "admintemp/view_complaints1.html", {'u': u})


#notification

def notificationpage(request):
    notify_form = Notification()
    if request.method == 'POST':
        notify_form = Notification(request.POST, request.FILES)
        if notify_form.is_valid():
            notify_form.save()
            messages.info(request, 'Add Successfully')
            return redirect('adminpage')
    return render(request, 'admintemp/add_notification.html', {'notify_form': notify_form})

#view notification

def notify_view(request):
    data = Notify.objects.all()
    return render(request, "admintemp/view_notify.html", {'data': data})


#remove police station

def removenotify(request, id):
    data = Notify.objects.get(id=id)
    data.delete()
    return redirect('notify_view')


#update police station

def updatenotify(request, id):
    notify = Notify.objects.get(id=id)
    notify_form = Notification(instance=notify)
    if request.method == 'POST':
        notify_form = Notification(request.POST,instance=notify)
        if notify_form.is_valid():
            notify_form.save()
            return redirect('notify_view')
    return render(request, 'admintemp/update_notification.html', {'notify_form': notify_form})