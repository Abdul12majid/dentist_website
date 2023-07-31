from django.db import models
from datetime import datetime

# Create your models here.
class Registered_doctor(models.Model):
	first_name=models.CharField('First Name', null=False, max_length=50)
	last_name=models.CharField('Second Name', null=False, max_length=50)

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Services_rendered(models.Model):
	services=models.CharField('SERVICES', null=False, max_length=70)
	doctor=models.ForeignKey(Registered_doctor, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.services}'

class Appointment_db(models.Model):
	service=models.ForeignKey(Services_rendered, blank=False, null=False, on_delete=models.CASCADE)
	doctor=models.ForeignKey(Registered_doctor, blank=False, null=False, on_delete=models.CASCADE)
	name=models.CharField('Name', null=False, max_length=50)
	email=models.EmailField('Email', null=False)
	appointment_date=models.DateTimeField('Date', default=datetime.now())

	def __str__(self):
		return f'{self.service} by {self.name} on the {self.appointment_date}'