from django.contrib import messages
from django.shortcuts import render, redirect

from detectionapp.forms import PoliceRegister, MissingPersons, ComplaintMessage
from detectionapp.models import Policereg, Complaint, Criminalreg, Addmissing, Notify, Detection


def policepage(request):
    return render(request, "policetemp/indexpolice.html")


#addmissingpersons

def addmissingpage(request):
    missing_form = MissingPersons()
    if request.method == 'POST':
        missing_form = MissingPersons(request.POST, request.FILES)
        if missing_form.is_valid():
            missing_form.save()
            messages.info(request, 'Registered Successfully')
            return redirect('policepage')
    return render(request, 'policetemp/addmissing.html', {'missing_form': missing_form})

#viewmissing persons

def missing_view(request):
    missingdata = Addmissing.objects.all()
    return render(request, "policetemp/view_missing.html", {'missingdata': missingdata})


#removemissingpersons

def removemissing(request, id):
    missingdata = Addmissing.objects.get(id=id)
    missingdata.delete()
    return redirect('missing_view')


#updatemissing persons

def updatemissing(request, id):
    missing = Addmissing.objects.get(id=id)
    missing_form = MissingPersons(instance=missing)
    if request.method == 'POST':
        missing_form = MissingPersons(request.POST,request.FILES, instance=missing)
        if missing_form.is_valid():
            missing_form.save()
            return redirect('missing_view')
    return render(request, 'policetemp/update_missing.html', {'missing_form': missing_form})


#view criminals details

def criminal_view1(request):
    criminaldata = Criminalreg.objects.all()
    return render(request, "policetemp/view_criminal.html", {'criminaldata': criminaldata})


#view public complaints

def complaint_view(request):
    u = Complaint.objects.all()
    return render(request, "policetemp/view_complaints.html", {'u': u})


#profile

def police_profile(request):
    police=request.user
    profile=Policereg.objects.filter(user=police)
    return render(request,'policetemp/profile.html', {'profile': profile})



#edit profile police


def editprofile(request, id):
    edit = Policereg.objects.get(id=id)
    edit_form = PoliceRegister(instance=edit)
    if request.method == 'POST':
        edit_form = PoliceRegister(request.POST,request.FILES, instance=edit)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('police_profile')
    return render(request, 'policetemp/edit_profile.html', {'edit_form': edit_form})

#public reply

def reply_complaint(request,id):
    complaint = Complaint.objects.get(id=id)
    if request.method == 'POST':
        r = request.POST.get('reply')
        complaint.reply = r
        complaint.save()
        messages.info(request,'Reply send for complaint')
        return redirect('complaint_view')
    return render(request,'policetemp/police_reply.html', {'complaint':complaint})


def notify_view1(request):
    data = Notify.objects.all()
    return render(request, "policetemp/view_notify1.html", {'data': data})

def detection_view(request):
    detectiondata = Detection.objects.all()
    return render(request, "policetemp/view_detection.html", {'detectiondata': detectiondata})