from django.test import TestCase
# from reservation.models import Reservation, OpeningHour
# from django.db.models import Count
# import datetime, pytz
#
# utc = pytz.utc
#
# def opening_hour_for_calendar():
#     start = (datetime.datetime.combine(datetime.date(2020, 4, 16), OpeningHour.objects.get(
#         day_week=datetime.datetime(2020, 4, 16).weekday()).opening_hours).replace(tzinfo=utc))
#     end = (datetime.datetime.combine(datetime.date(2020, 4, 16), OpeningHour.objects.get(
#         day_week=datetime.datetime(2020, 4, 16).weekday()).closing_hours).replace(tzinfo=utc))
#     today_time = []
#     while start <= end:
#         today_time.append(start)
#         start += datetime.timedelta(minutes=15)
#     return today_time
#
#
# def check_if_taken(reservations, hour, machine):
#     for reservation in reservations:
#         if reservation.starting_hours <= hour <= reservation.finishing_hours and machine[0] == reservation.machineID_id:
#             return reservation.userID
#
#
#
# from django.shortcuts import render
# from reservation.models import Reservation, OpeningHour
# import datetime, pytz
# from django.db.models import Count
# # Create your views here.
# utc = pytz.utc
#
#
# utc = pytz.utc
#
# def create_list_opening_hour_for_calendar():
#     start = (datetime.datetime.combine(datetime.date(2020, 4, 16), OpeningHour.objects.get(
#         day_week=datetime.datetime(2020, 4, 16).weekday()).opening_hours).replace(tzinfo=utc))
#     end = (datetime.datetime.combine(datetime.date(2020, 4, 16), OpeningHour.objects.get(
#         day_week=datetime.datetime(2020, 4, 16).weekday()).closing_hours).replace(tzinfo=utc))
#     today_time = []
#     while start <= end:
#         today_time.append(start)
#         start += datetime.timedelta(minutes=15)
#     return today_time
#
#
# def check_if_taken(reservations, hour, machine):
#     for reservation in reservations:
#         if machine == reservation.machineID_id and reservation.starting_hours <= hour < reservation.finishing_hours:
#             return reservation.userID
#
#
# def generate_today_reservation():
#     today_machine_id = [machine[0] for machine in
#                      Reservation.objects.filter(date='2020-04-16').values_list('machineID').annotate(
#                          reservationcount=Count('machineID'))]
#     today_reservation = Reservation.objects.filter(date='2020-04-16').order_by('starting_hours')
#     today_time = create_list_opening_hour_for_calendar()
#     calendar_time = []
#
#     for machine_id in today_machine_id:
#         counter = 1
#         user_check = None
#         for hour in today_time:
#             user = check_if_taken(today_reservation, hour, machine_id)
#             if user and user_check == user:
#                 time = {
#                         'hour': hour,
#                         'machine_id': machine_id,
#                         'user' : user,
#                         'taken': 'yes',
#                         'counter': counter
#                         }
#                 calendar_time.append(time)
#                 counter += 1
#             elif user and user_check != user:
#                 time = {
#                         'hour': hour,
#                         'machine_id': machine_id,
#                         'user' : user,
#                         'taken': 'yes',
#                         'counter': counter
#                         }
#                 calendar_time.append(time)
#                 counter += 1
#                 user_check = user
#             else:
#                 time = {
#                         'hour': hour,
#                         'machine_id': machine_id,
#                         'taken': 'no'
#                         }
#                 calendar_time.append(time)
#                 counter = 1
#                 user_check = None
#     return calendar_time
#
#
#
#
# print(generate_today_reservation())

# today_machine = [{'machineID': machine.machineID}
#                  for machine in
#                  Reservation.objects.filter(date='2020-04-16').distinct()]
#
# today_reservation = [{'machineID': reservation.machineID,
#                       'user': reservation.userID,
#                       'starting_hour': reservation.starting_hours,
#                       'finishing_hour': reservation.finishing_hours
#                       }
#                      for reservation in
#                      Reservation.objects.filter(date='2020-04-16').order_by('starting_hours')]