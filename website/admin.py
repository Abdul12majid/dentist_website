from django.contrib import admin
from .models import Registered_doctor, Appointment_db, Services_rendered
# Register your models here.
@admin.register(Registered_doctor)
class Registered_doctors_Admin(admin.ModelAdmin):
	pass


@admin.register(Services_rendered)
class Services_rendered_Admin(admin.ModelAdmin):
	pass


@admin.register(Appointment_db)
class Appointment_db_Admin(admin.ModelAdmin):
	pass