from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import reservation_with_badge, reservation_without_badge
from .validation_script import get_valid_days_form_validation, validate_type_reservation, validate_minute_duration
from django.contrib import messages
from .script import get_available_spots_for_machine
from machines.models import Machine
import locale
import datetime
from reservation.models import Reservation, TypeReservation
from accounts.models import Patron
from datetime import timedelta
from django.core.mail import send_mail
import pytz

est = pytz.timezone('America/Montreal')

class DurationListView(CreateView):
    form_class = reservation_with_badge
    success_url = reverse_lazy('duration_changelist')


def load_durations(request):
    type_reservation_id = request.GET.get('reservationID')
    duration = TypeReservation.objects.get(id=type_reservation_id)
    duration_list = []
    while duration.min_duration <= duration.max_duration:
        duration_list.append(duration.min_duration)
        duration.min_duration += timedelta(minutes=15)
    return render(request, 'reservation/duration_dropdown_list_options.html', {'durations': duration_list})


def display_reservation_form(request, machineID):
    template_name, context = None, None
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        date = datetime.datetime.strptime(request.POST['dates'], '%Y-%m-%d').date()
        valid_dates = get_valid_days_form_validation()
        if not Patron.objects.filter(user=request.user, badges__machineID=machineID):
            if date in valid_dates:
                machine_infos = Machine.objects.get(id=machineID)
                template_name = 'reservation/list_by_date.html'
                context = {'available_spots': get_available_spots_for_machine(date=request.POST['dates'],
                                                                              minute_duration='1:00:00', staff_point=5,
                                                                              type_reservation='Formation',
                                                                              machine=machineID),
                           'machine': machine_infos}
                return render(request, template_name, context=context)
            else:

                return HttpResponse('No such Author Found!')

        else:
            if validate_type_reservation(machineID, request.POST.get('type_reservation')) and \
                    validate_minute_duration(request.POST.get('type_reservation'), request.POST.get('duration')) and\
                    date in valid_dates:

                machine_infos = Machine.objects.get(id=machineID)
                type_reservation = TypeReservation.objects.get(id=request.POST.get('type_reservation'))
                template_name = 'reservation/list_by_date.html'
                context = {'available_spots': get_available_spots_for_machine(date=request.POST['dates'],
                                                                              minute_duration=
                                                                              request.POST.get('duration'),
                                                                              staff_point=type_reservation.staff_point,
                                                                              machine=machineID,
                                                                              type_reservation=type_reservation),
                           'machine': machine_infos}
                return render(request, template_name, context=context)
            else:
                return HttpResponse('No such Author Found!')

    if request.method == 'GET':
        if not Patron.objects.filter(user=request.user, badges__machineID=machineID):
            form = reservation_without_badge()
            machine_infos = Machine.objects.values_list('context_without_badge', 'name', 'id').get(id=machineID)
            context = {'machine': machine_infos,
                       'form': form}
            template_name = 'reservation/list.html'
            return render(request, template_name, context)
        else:
            form = reservation_with_badge(machineID)
            machine_infos = Machine.objects.values_list('context_with_badge', 'name', 'id').get(id=machineID)
            context = {'machine': machine_infos,
                       'form': form}
            template_name = 'reservation/list.html'
            return render(request, template_name, context)




def reservation_done(request):
    if request.method == 'POST':

        if request.user.is_authenticated:

            userID = request.user
            date = request.POST['date']
            machineID = get_object_or_404(Machine, pk=request.POST['machine'])
            starting_hours = est.localize(datetime.datetime.strptime(request.POST['start_time'], '%Y-%m-%d %H:%M'))
            finishing_hours = est.localize(datetime.datetime.strptime(request.POST['end_time'], '%Y-%m-%d %H:%M'))
            staff_points = request.POST['staff_point']
            type_reservation = request.POST['type_reservation']
            type_reservation_id = TypeReservation.objects.get(type=type_reservation).id
            date_validation = datetime.datetime.strptime(request.POST['date'], '%Y-%m-%d').date()
            valid_dates = get_valid_days_form_validation()
            duration = finishing_hours - starting_hours
            reservation_from_user = Reservation.objects.all().filter(userID=userID, date=date)

            if reservation_from_user:
                messages.error(request, 'Désolé ! Vous ne pouvez faire qu\'une réservation par jour')
                return redirect('/reservation/' + str(machineID.id))

            if validate_type_reservation(request.POST.get('machine'), type_reservation_id) and \
                    validate_minute_duration(type_reservation_id, duration) and\
                    date_validation in valid_dates:

                reservation = Reservation(userID=userID, machineID=machineID, date=date, starting_hours=starting_hours,
                                          finishing_hours=finishing_hours, staff_points=staff_points,
                                          type_reservation=type_reservation)
                reservation.save()

                # Configure la langue en français pour datetime
                locale.setlocale(locale.LC_TIME, "fr_FR")

                send_mail(
                    'Réservation Fab Lab',
                    'Vous avez procédé à une réservation au Fab Lab de Brossard le {} de {} à {} pour la machine {}.'.format(
                        date, starting_hours, finishing_hours, machineID.name),
                    'bibliotheque@brossard.ca',
                    [userID.email],
                    fail_silently=False
                )

                messages.success(request, 'Votre réservation a été ajoutée !')
                return redirect("dashboard")

            else:
                messages.error(request, 'Ne joue pas avec mes formulaires')
                return redirect('/reservation/' + str(machineID.id))
        else:
            messages.error(request, "Vous devez être connecté pour faire une réservation.")
            return redirect('login')
    else:
        return redirect("reservations")

    return render(request, 'reservation/done.html')
