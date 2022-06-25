import datetime
from reservation.models import OpeningHour, Holiday, TypeReservation, Reservation
from machines.models import Machine
from reservation.script import get_staff_point_in_use, get_opening_closing_hours, generate_max_staff_point

hours = get_opening_closing_hours('2021-08-19')
start = hours['opening_hours']
end = hours['closing_hours']
date = '2021-08-19'

max_staff_points = generate_max_staff_point(date, start, end)

def get_reservations(date):
    final_staff_points = []
    # getting a list of staff_point by 15 minutes
    for reservation in Reservation.objects.filter(date=date).order_by('starting_hours'):
        start = reservation.starting_hours
        end = reservation.finishing_hours
        while start <= end:
            staff_point = {
                'starting_hour': start,
                'staff_point': reservation.staff_points,
                'reservation_id': reservation.id,
                'machineID': reservation.machineID
            }
            final_staff_points.append(staff_point)
            start += datetime.timedelta(minutes=15)
    return final_staff_points

print(get_reservations('2021-08-19'))
print(max_staff_points)

