import re


from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

from detectionapp.models import Login, Policereg, Criminalreg, Addmissing, Complaint, Publicreg, Notify, Detection


class LoginForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm password")

    class Meta:
        model = Login
        fields = ("username", "password1", "password2")

def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')

# def validate_pin(pin):
#     return bool(re.fullmatch("\d{4}|\d{6}", pin))

def validate_pin(value):
    if not re.compile(r'^[1-9][0-9]{5}$').match(value):
        raise ValidationError('This is Not a Valid Pin Code')

class PoliceRegister(forms.ModelForm):
    phone_number = forms.CharField(validators=[phone_number_validator])
    pin_code = forms.CharField(validators=[validate_pin])

    class Meta:
        model = Policereg
        fields = ('state','District','station_name', 'address', 'pin_code', 'phone_number', 'email', 'photo')


class CriminalRegister(forms.ModelForm):
    # phone_number = forms.CharField(validators=[phone_number_validator])
    class Meta:
        model = Criminalreg
        fields = ('station_name','state','District','name','gender','crime_no','crime_category','photo')

class MissingPersons(forms.ModelForm):
    class Meta:
        model = Addmissing
        fields = ('station_name','name','gender','state','District','crime_no','crime_category','photo')

class ComplaintMessage(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('user','date','complaint_msg')

class PublicRegister(forms.ModelForm):
    phone_number = forms.CharField(validators=[phone_number_validator])
    pin_code = forms.CharField(validators=[validate_pin])

    class Meta:
        model = Publicreg
        fields = ('name','gender','address','pin_code','District','state','phone_number','email','photo','aadhar')



class Notification(forms.ModelForm):
    class Meta:
        model = Notify
        fields = ('date','Notification_message')

class DetectionMessage(forms.ModelForm):
    class Meta:
        model = Detection
        fields = ('crime_no', 'name','location')