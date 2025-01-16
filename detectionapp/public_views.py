from django.contrib import messages
from django.shortcuts import render, redirect

from detectionapp.forms import ComplaintMessage, PublicRegister, LoginForm, DetectionMessage
from detectionapp.models import Complaint, Criminalreg, Addmissing, Publicreg, Notify


def publicpage(request):
    return render(request, "publictemp/indexpublic.html")


#public regidtration


def publicregpage(request):
    user_form = LoginForm()
    public_form = PublicRegister()
    if request.method == 'POST':
        user_form = LoginForm(request.POST)
        public_form = PublicRegister(request.POST, request.FILES)
        if user_form.is_valid() and public_form.is_valid():
            user = user_form.save(commit=False)
            user.is_public = True
            user.save()
            public = public_form.save(commit=False)
            public.user = user
            public_form.save()
            messages.info(request, 'Registered Successfully')
            return redirect('loginpage')
    return render(request, 'publictemp/public_registration.html', {'user_form': user_form, 'public_form': public_form})


#view missing persons details

def missing_view1(request):
    missingdata = Addmissing.objects.all()
    return render(request, "publictemp/view_missing1.html", {'missingdata': missingdata})

#view criminals details

def criminal_view2(request):
    criminaldata = Criminalreg.objects.all()
    return render(request, "publictemp/view_criminal1.html", {'criminaldata': criminaldata})


#add complaints

def complaintpage(request):
    complaint_form = ComplaintMessage()
    u=request.user
    print(u)
    if request.method == 'POST':
        complaint_form = ComplaintMessage(request.POST)
        if complaint_form.is_valid():
            obj = complaint_form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Thank you.....!!!')
            return redirect('public_page')
    else:
        complaint_form = ComplaintMessage()
    return render(request, 'publictemp/add_complaint.html', {'complaint_form': complaint_form})


##view complaint public

def complaint_view2(request):
    u = Complaint.objects.filter(user=request.user)
    return render(request, 'publictemp/viewpublic_complaint.html', {'u': u})

#profile

def public_profile(request):
    public=request.user
    profile=Publicreg.objects.filter(user=public)
    return render(request,'publictemp/public_profile.html', {'profile': profile})

#edit profile


def editpublicprofile(request, id):
    edit = Publicreg.objects.get(id=id)
    edit_form = PublicRegister(instance=edit)
    if request.method == 'POST':
        edit_form = PublicRegister(request.POST,request.FILES, instance=edit)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('public_profile')
    return render(request, 'publictemp/edit_publicprofile.html', {'edit_form': edit_form})


# view notification

def notify_view2(request):
    data = Notify.objects.all()
    return render(request, "publictemp/view_notification.html", {'data': data})



def detectionpage(request):
    detection_form = DetectionMessage()
    u=request.user
    print(u)
    if request.method == 'POST':
        detection_form = DetectionMessage(request.POST)
        if detection_form.is_valid():
            obj = detection_form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, 'Thank you.....!!!')
            return redirect('public_page')
    else:
        detection_form = DetectionMessage()
    return render(request, 'publictemp/detect_location.html', {'detection_form': detection_form})

def detect(request):
    import time

    import cv2
    import numpy as np
    import face_recognition
    import os

    path = 'media/image/criminal'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)
    print(type(classNames))

    def findEncodings(images):
        encodeList = []

        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)
            print(matchIndex)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                # print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                # if (label == 0):
                #     num = 'MY'
                #     value = write_read(num)
                #     break
                # elif (label == 1):
                #     num = 'NM'
                #     value = write_read(num)
                #     break

        cv2.imshow('Webcam', img)
        if cv2.waitKey(1) == ord("q"):
            return redirect("criminal_view2")
            break
    return render(request,'publictemp/detect.html')

def det(request):
    return render(request,'publictemp/detect.html')