from django import forms
from django.forms import ModelForm
from .models import Appointment_db, Services_rendered
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AddAppointmentForm(ModelForm):
	class Meta:
		model=Appointment_db
		fields=('service','doctor', 'name', 'email',)

		labels={
		'service':'Select service',
		'doctor':'Select doctor',
		'name':'Name',
		'email':'Email',
		}

		widgets={
		'service':forms.Select(attrs={'class':'form-select bg-light border-0', 'style':'height:55px;', 'placeholder':'select-service'}),
		'doctor':forms.Select(attrs={'class':'form-select bg-light border-0', 'style':'height:55px;', 'placeholder':'select-doctor'}),
		'name':forms.TextInput(attrs={'class':'form-select bg-light border-0', 'style':'height:55px;', 'placeholder':'your name'}),
		'email':forms.TextInput(attrs={'class':'form-select bg-light border-0', 'style':'height:55px;', 'placeholder':'your email'}),
		}

class SearchDoctorForm(ModelForm):
	class Meta:
		model=Services_rendered
		fields=('services',)

		labels={
		'services':'Select service'
		}

		widgets={
		'service':forms.Select(attrs={'class':'form-select bg-light border-0 mb-3', 'style':'height:40px;'})
		}

class RegisterUserForm(UserCreationForm):
	email=forms.EmailField(min_length=10, widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name=forms.CharField(min_length=4, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name=forms.CharField(min_length=4, widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model=User
		fields=('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class']='form-control'
		self.fields['password1'].widget.attrs['class']='form-control'
		self.fields['password2'].widget.attrs['class']='form-control'








