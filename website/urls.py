from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login-user'),
    path('base', views.base, name="base"),
    path('price', views.price, name="prices"),
    path('team', views.team, name="team"),
    path('testimonial', views.testimonial, name="testimonial"),
    path('appointment', views.appointment_db, name="appointment"),
    path('about', views.about, name="about"),
    path('service', views.service, name="service"),
    path('contact', views.contact, name="contact"),
    path('register_user', views.register_user, name="register-user"),
    path('logout_user', views.logout_user, name="logout-user"),
    path('login', views.login2, name='login'),

   # path('appointment_db', views.appointment_db, name="appointment-db"),
]
