import datetime
from .models import OpeningHour, Reservation, Staff
from machines.models import Machine
import pytz

est = pytz.timezone('America/Montreal')


def get_opening_closing_hours(date):
    hours = {}
    datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
    # get day of the week
    weekday = datetime_obj.weekday()
    # get opening hours for the day and add timezone info
    for i in OpeningHour.objects.filter(day_week=weekday):
        hours = {
            'opening_hours': est.localize(datetime.datetime.combine(datetime_obj, i.opening_hours)),
            'closing_hours': est.localize(datetime.datetime.combine(datetime_obj, i.closing_hours))
        }
    return hours


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
                'machineID': reservation.machineID_id
            }
            final_staff_points.append(staff_point)
            start += datetime.timedelta(minutes=15)
    return final_staff_points


def get_staff_point_in_use(start, duration, reservations, staff_point):
    staff_point = staff_point
    reservations_id = []
    for reservation in reservations:
        starting_hour = reservation['starting_hour']
        if start < starting_hour < start + duration and reservation['reservation_id'] not in reservations_id:
            staff_point = staff_point + reservation['staff_point']
            reservations_id.append(reservation['reservation_id'])
    return staff_point


def check_if_enough_machine(start, duration, machine, reservations):
    reservations_id = []
    number_reservation_for_machine = 0
    for reservation in reservations:
        starting_hour = reservation['starting_hour']
        if start < starting_hour < start + duration and reservation['machineID'] == machine and reservation['reservation_id'] not in reservations_id:
            number_reservation_for_machine += 1
            reservations_id.append(reservation['reservation_id'])
    return number_reservation_for_machine


def get_staff_schedule(date):
    datetime_obj = datetime.datetime.strptime(date, '%Y-%m-%d')

    # get day of the week
    weekday = datetime_obj.weekday()
    staffs = Staff.objects.filter(day_week=weekday).values('shift_start', 'shift_end', 'staffID__staff_point')

    for staff in staffs:
            staff['shift_start'] = est.localize(datetime.datetime.combine(datetime_obj, staff['shift_start']))
            staff['shift_end'] = est.localize(datetime.datetime.combine(datetime_obj, staff['shift_end']))

    return staffs


def get_staff_points_at_specific_time(time, staffs):
    staff_point = 0
    for staff in staffs:
        if staff['shift_start'] <= time < staff['shift_end']:
            staff_point += staff['staffID__staff_point']
    return staff_point


def generate_max_staff_point(date, start, end):
    staff_schedule = get_staff_schedule(date)
    max_staff_point = {}
    while start <= end:
        max_staff_point[start] = {
            'staff_point': get_staff_points_at_specific_time(start, staff_schedule)
        }
        start += datetime.timedelta(minutes=15)
    return max_staff_point


def check_if_enough_staff(start, duration, staff_point_in_use, max_staff_points):
    end = start + duration
    while start <= end:
        if max_staff_points[start]['staff_point'] < staff_point_in_use:
            return False
        start += datetime.timedelta(minutes=15)
    return True


def get_available_spots_for_machine(date, minute_duration, staff_point, machine, type_reservation):
    available_spots = []
    hours = get_opening_closing_hours(date)
    start = hours['opening_hours']
    end = hours['closing_hours']
    duration1 = datetime.datetime.strptime(minute_duration, '%H:%M:%S')
    max_staff_points = generate_max_staff_point(date, start, end)
    duration = datetime.timedelta(hours=duration1.hour, minutes=duration1.minute)
    reservations = get_reservations(date)
    number_machine = Machine.objects.get(id=machine).number_machine
    while start + duration <= end:
        staff_point_in_use = get_staff_point_in_use(start, duration, reservations, staff_point)
        if check_if_enough_staff(start, duration, staff_point_in_use,
                                 max_staff_points) and check_if_enough_machine(start, duration, machine,
                                                                               reservations) < number_machine:
            available_spot = {'start': start,
                              'end': start + duration,
                              'date': date,
                              'staff_point': staff_point,
                              'type_reservation': type_reservation}
            available_spots.append(available_spot)

        else:
            pass
        start += datetime.timedelta(minutes=15)
    return available_spots
