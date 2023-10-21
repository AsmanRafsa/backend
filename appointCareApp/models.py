from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

def upload_to(instance,filename):
    return "hospitals/{filename}".format(filename=filename)

class HospitalManager(BaseUserManager):
    def create_user(self, email, phone_number, name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, phone_number=phone_number, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, phone_number, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, phone_number, name, password, **extra_fields)

class Hospital(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = HospitalManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone_number', 'name']

    def __str__(self):
        return self.name
    

class HospitalDetails(models.Model):
    hospital=models.OneToOneField(Hospital, on_delete=models.CASCADE)
    hospital_Image=models.ImageField(("image"),upload_to=upload_to,default="hospitals/")
    hospital_Location=models.CharField(max_length=60)
    hospital_Slogan=models.CharField(max_length=100, blank=True)
    hospital_Description=models.TextField()

    def __str__(self):
        return 'hospital details'
    

class DoctorsDetails(models.Model):
    doctorImage=models.ImageField(("image"),upload_to=upload_to,default="hospitals/")
    doctorName=models.CharField(max_length=50)
    doctorSpeciality=models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='doctors')

    def __str__(self):
        return self.doctorName



class PatientDetails(models.Model):
    patientName = models.CharField(max_length=255)
    patientDisease=models.TextField()
    patientContact=models.CharField(max_length=15)
    patientAge = models.PositiveIntegerField()
    timeBooked=models.DateTimeField(default=timezone.now())
    patientDoctor=models.CharField(max_length=50)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name='patient')

    def __str__(self):
        return self.patientName



