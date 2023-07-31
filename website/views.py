from django.shortcuts import render, redirect
from .forms import AddAppointmentForm, SearchDoctorForm, RegisterUserForm
from django.http import HttpResponseRedirect
from .models import Services_rendered, Registered_doctor, Appointment_db
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
#def home(request):
	#our_services=Services_rendered.objects.all()
	#return render(request, 'home.html', {'our_services':our_services})

def base(request):
	return render(request, 'base.html', {})

def price(request):
	if request.user.is_authenticated:
		return render(request, "price.html", {})
	else:
		messages.success(request, ('Login to access this page.'))
		return redirect('login')

def team(request):
	if request.user.is_authenticated:
		return render(request, "home.html", {})
	else:
		messages.success(request, ('Login to access this page.'))
		return redirect('login')

def testimonial(request):
	if request.user.is_authenticated:
		return render(request, "testimonial.html", {})
	else:
		messages.success(request, ('Login to access this page.'))
		return redirect('login')

def appointment(request):
	if User.is_authenticated:
		if request.method=="POST":
			service=request.POST['select-service']
			doctor=request.POST['select-doctor']
			your_name=request.POST['your-name']
			your_email=request.POST['your-email']
			date_of=request.POST['date']
			time_of=request.POST['time']
			return render(request, "appointment.html", {'service':service, 'your_name':your_name, 'your_email':your_email, 'date_of':date_of, 'time_of':time_of})
		    
		else:
			return render(request, 'appointment.html', {})
	else:
		messages.success(request, ("You can't access this page without Logging in"))
		return HttpResponseRedirect('/')
	#return render(request, 'appointment.html', {})

def about(request):
	if request.user.is_authenticated:
		return render(request, 'about.html', {})
	else:
		messages.success(request, ("You can't access this page without Logging in"))
		return HttpResponseRedirect('/')

def service(request):
	if request.user.is_authenticated:
		return render(request, 'service.html', {})
	else:
		messages.success(request, ("You can't access this page without Logging in"))
		return HttpResponseRedirect('/')

def contact(request):
	if request.method=="POST":
		your_name=request.POST['your-name']
		your_email=request.POST['your-email']
		message_title=request.POST['title']
		your_message=request.POST['your-message']
		return render(request, 'contact.html', {'your_name':your_name})
	else:
		return render(request, 'contact.html', {})
	

def appointment_db(request):
	
	#messages.success(request, "You can't access this page")
	if request.user.is_authenticated:
		if request.method=='POST':
			form=AddAppointmentForm(request.POST)
			if form.is_valid():
				user=Appointment_db.objects.filter(email=form.cleaned_data['email']).exists()
				name=form.cleaned_data['name']
				if not user:
					form.save()
					messages.success(request, (f'Good day {name}, your apppointment has been submitted, kindly await reply.'))
					return HttpResponseRedirect('/appointment')
				else:
					messages.success(request, ('Pending apppointment made for this patient.'))
					return HttpResponseRedirect('/appointment')
		else:
			form=AddAppointmentForm()
			return render(request, 'appointment_db.html', {'form':form})
	else:
		messages.success(request, "You can't access this page without Logging in.")
		return HttpResponseRedirect('/login')

def home(request):
	our_services=Services_rendered.objects.all()
	if request.method=='POST':
		keyword=request.POST['search-doctor']
		all_services=Services_rendered.objects.filter(services__contains=keyword)
		return render(request, 'home.html', {'all_services':all_services, 'keyword':keyword,})
	else:
		return render(request, 'home.html', {'our_services':our_services})

def login_user(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Login Successful'))
			return redirect('about')
		else:
			messages.success(request, ("Error Logging In"))
			return HttpResponseRedirect('/')
	else:
		return render(request, "home.html", {})
	

def logout_user(request):
	if request.user.is_authenticated:
		logout(request)
		messages.success(request, ("You're logged out"))
		return HttpResponseRedirect('/login')
	else:
		messages.success(request, ("You're logged out already"))
		return render(request, "login.html", {})


def register_user(request):
	if request.method=='POST':
		form=RegisterUserForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data['username']
			password=form.cleaned_data['password1']
			user=authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Account Created Successfully"))
			return HttpResponseRedirect('/')
		else:
			messages.success(request, ('Error with details provided'))
			return redirect('register-user')
	else:
		form=RegisterUserForm()
	return render(request, 'register.html', {'form':form})

def login2(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, ('Login Successful'))
			return redirect('about')
		else:
			messages.success(request, ('Error Logging in'))
			return redirect('login')
	else:
		return render(request, "login.html", {})
