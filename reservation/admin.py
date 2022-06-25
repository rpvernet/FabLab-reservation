from django.contrib import admin

# Register your models here.
from .models import Reservation, Holiday, OpeningHour, TypeReservation, Badges, Staff

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('machineID', 'date', 'starting_hours', 'finishing_hours', 'staff_points', 'userID')
    list_display_links = ('machineID',)
    search_fields = ('starting_hours', 'machineID')

class OpeningHoursAdmin(admin.ModelAdmin):
    list_display = ('day_week', 'opening_hours', 'closing_hours')
    list_display_links = ('day_week',)
    search_fields = ('day_week', 'opening_hours')

class ReservationTypeAdmin(admin.ModelAdmin):
    list_display = ('type','min_duration', 'max_duration', 'staff_point')
    list_display_links = ('type',)
    search_fields = ('type', 'min_duration')

class StaffAdmin(admin.ModelAdmin):
    list_display = ('day_week', 'staffID', 'shift_start', 'shift_end')
    list_display_links = ('day_week',)
    search_fields = ('day_week', 'staff_id')



admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Holiday)
admin.site.register(OpeningHour, OpeningHoursAdmin)
admin.site.register(TypeReservation, ReservationTypeAdmin)
admin.site.register(Badges)
admin.site.register(Staff, StaffAdmin)
