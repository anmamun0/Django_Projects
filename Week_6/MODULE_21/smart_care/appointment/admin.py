from django.contrib import admin


from .models import Appointment
# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','patient_name','appointment_types','appointment_status']
    def patient_name(slef,obj):
        return obj.patient.user.first_name
    
    def doctor_name(slef,obj):
        return obj.doctor.user.first_name
    

admin.site.register(Appointment,AppointmentAdmin)


