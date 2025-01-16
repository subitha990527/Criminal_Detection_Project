from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_police=models.BooleanField(default=False),
    is_public=models.BooleanField(default=False)

# police registration.
class Policereg(models.Model):
    user=models.OneToOneField(Login,on_delete=models.CASCADE,related_name="police")
    station_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    pin_code=models.CharField(max_length=100)
    state=models.CharField(max_length=100,default='Kerala')
    dist = (('TRIVANDRUM','TRIVANDRUM'),('KOLLAM','KOLLAM'),('PATHANAMTHITTA','PATHANAMTHITTA'),('IDUKKI','IDUKKI'),('ALAPPUZHA','ALAPPUZHA'),('PALAKKAD','PALAKKAD'),('THRISSUR','THRISSUR'),('ERNAKULAM','ERNAKULAM'),('MALAPPURAM','MALAPPURAM'),('WAYANAD','WAYANAD'),('KOTTAYAM','KOTTAYAM'),('KOZHIKODE','KOZHIKODE'),('KANNUR','KANNUR'),('KASARAGOD','KASARAGODE'))
    District = models.CharField(max_length=50,choices=dist,null=True)
    phone_number=models.CharField(max_length=100)
    email=models.EmailField()
    photo=models.ImageField(upload_to='image')


    def __str__(self):
        return self.station_name

class Publicreg(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name="public")
    name = models.CharField(max_length=100)
    gender1 = (('MALE','MALE'),('FEMALE','FEMALE'),('OTHERS','OTHERS'))
    gender = models.CharField(max_length=100, choices=gender1, null=True)
    address = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=100)
    state = models.CharField(max_length=100,default='kerala')
    dist1 = (
    ('TRIVANDRUM', 'TRIVANDRUM'), ('KOLLAM', 'KOLLAM'), ('PATHANAMTHITTA', 'PATHANAMTHITTA'), ('IDUKKI', 'IDUKKI'),
    ('ALAPPUZHA', 'ALAPPUZHA'), ('PALAKKAD', 'PALAKKAD'), ('THRISSUR', 'THRISSUR'), ('ERNAKULAM', 'ERNAKULAM'),
    ('MALAPPURAM', 'MALAPPURAM'), ('WAYANAD', 'WAYANAD'), ('KOTTAYAM', 'KOTTAYAM'), ('KOZHIKODE', 'KOZHIKODE'),
    ('KANNUR', 'KANNUR'), ('KASARAGOD', 'KASARAGODE'))
    District = models.CharField(max_length=50, choices=dist1, null=True)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='image')
    aadhar = models.FileField(upload_to='image')

    def __str__(self):
        return self.name

# criminal registration.
class Criminalreg(models.Model):
    station_name = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default='kerala')
    dist1 = (
        ('TRIVANDRUM', 'TRIVANDRUM'), ('KOLLAM', 'KOLLAM'), ('PATHANAMTHITTA', 'PATHANAMTHITTA'), ('IDUKKI', 'IDUKKI'),
        ('ALAPPUZHA', 'ALAPPUZHA'), ('PALAKKAD', 'PALAKKAD'), ('THRISSUR', 'THRISSUR'), ('ERNAKULAM', 'ERNAKULAM'),
        ('MALAPPURAM', 'MALAPPURAM'), ('WAYANAD', 'WAYANAD'), ('KOTTAYAM', 'KOTTAYAM'), ('KOZHIKODE', 'KOZHIKODE'),
        ('KANNUR', 'KANNUR'), ('KASARAGOD', 'KASARAGODE'))
    District = models.CharField(max_length=50, choices=dist1, null=True)
    name = models.CharField(max_length=100)
    gender1 = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS'))
    gender = models.CharField(max_length=100, choices=gender1, null=True)
    crime_no = models.CharField(max_length=100)
    crime_category = models.CharField(max_length=100)
    # photo = models.ImageField(upload_to='image')
    photo=models.ImageField(upload_to='image/criminal')



    def __str__(self):
        return self.name

# missing and wanted person

class Addmissing(models.Model):
    station_name = models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    gender1 = (('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS'))
    gender = models.CharField(max_length=100, choices=gender1, null=True)
    state=models.CharField(max_length=100,default='kerala')
    dist1 = (
        ('TRIVANDRUM', 'TRIVANDRUM'), ('KOLLAM', 'KOLLAM'), ('PATHANAMTHITTA', 'PATHANAMTHITTA'), ('IDUKKI', 'IDUKKI'),
        ('ALAPPUZHA', 'ALAPPUZHA'), ('PALAKKAD', 'PALAKKAD'), ('THRISSUR', 'THRISSUR'), ('ERNAKULAM', 'ERNAKULAM'),
        ('MALAPPURAM', 'MALAPPURAM'), ('WAYANAD', 'WAYANAD'), ('KOTTAYAM', 'KOTTAYAM'), ('KOZHIKODE', 'KOZHIKODE'),
        ('KANNUR', 'KANNUR'), ('KASARAGOD', 'KASARAGODE'))
    District = models.CharField(max_length=50, choices=dist1, null=True)
    crime_no=models.CharField(max_length=100)
    crime_category=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='image')

    def __str__(self):
        return self.name

#user complaint registration

class Complaint(models.Model):
    user = models.ForeignKey(Login,on_delete=models.DO_NOTHING)
    date = models.DateField(max_length=100)
    complaint_msg = models.TextField(max_length=100)
    reply=models.TextField(null=True,blank=True)


    # def __str__(self):
    #     return self.name
    #

#add notification

class Notify(models.Model):
    date = models.DateField(max_length=100)
    Notification_message = models.CharField(max_length=100)


class Detection(models.Model):
    crime_no = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)


