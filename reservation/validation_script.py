from reservation.models import OpeningHour, Holiday, TypeReservation
from machines.models import Machine
import datetime

base = datetime.date.today()


def format_date_for_django_form_validation(date_time):
    return date_time


def get_valid_days_form_validation():
    valid_weekday = OpeningHour.objects.exclude(opening_hours='00:00').values_list('day_week', flat=True)
    all_days = [base + datetime.timedelta(days=x) for x in range(14)]
    holidays = Holiday.objects.all().values_list('date', flat=True)
    valid_days = [format_date_for_django_form_validation(day) for day in all_days if
                  day.weekday() in valid_weekday and day not in holidays]
    return valid_days


def validate_type_reservation(machineID, type_reservation_request):
    type_reservation_for_machine = []
    for i in Machine.objects.filter(id=int(machineID)).values('typeReservation'):
        type_reservation_for_machine.append(i['typeReservation'])

    if int(type_reservation_request) in type_reservation_for_machine:
        return True


def validate_minute_duration(type_reservation, minute_duration):
    try:

        delta = datetime.datetime.strptime(minute_duration, "%H:%M:%S")
        delta = datetime.timedelta(hours=delta.hour, minutes=delta.minute, seconds=delta.second)

    except:
        delta = minute_duration

    time_frame = {}
    for i in TypeReservation.objects.filter(id=type_reservation).values('min_duration', 'max_duration'):
        time_frame = {
            'min_duration': i['min_duration'],
            'max_duration': i['max_duration']
        }

    if time_frame['min_duration'] <= delta <= time_frame['max_duration']:
        return True


