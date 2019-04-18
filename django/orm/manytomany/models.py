from django.db import models

# Create your models here.

# 병원에 오는 사람들을 기록하는 시스템을 만들려고 한다.
# 필수적인 모델은 환자와 의사이다.
# 어떤 한 관게로 표현할 수 있을까? M:N

class Doctor(models.Model):
    name = models.TextField()

    
class Patient(models.Model):
    name = models.TextField()
    doctors = models.ManyToManyField(Doctor, related_name = 'patients', through='Reservation') # M:N 관계형성. 
    # M:N 관계를 만들 때 위 코드 대신 Doctor에 Patients하고 Patient에 안하는 방식도 가능하다.

    
# Doctor:Reservation = 1:M -> Reservation = M*Doctor
# Patient:Reservation = 1:N -> Reservation = N*Patient
# M*Doctor = N*Patient -> M:N = Doctor:Patient
# Doctor:Patient = M:N 
class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
        