from django import forms
from django.db.models import Prefetch
from django.forms import ModelChoiceField
from machines.models import Machine
from reservation.models import TypeReservation
from reservation.models import OpeningHour, Holiday
from django.core.exceptions import ValidationError
import datetime

base = datetime.date.today()

date_list = [(datetime.date(2021, 1, 2), '2021-01-02'), (datetime.date(2021, 1, 7), '2021-01-07'),
             (datetime.date(2021, 1, 8), '2021-01-08'), (datetime.date(2021, 1, 9), '2021-01-09'),
             (datetime.date(2021, 1, 14), '2021-01-14'), (datetime.date(2021, 1, 15), '2021-01-15')]


def format_date_for_django_form(date_time):
    return date_time, date_time


def get_valid_days():
    valid_weekday = OpeningHour.objects.exclude(opening_hours='00:00').values_list('day_week', flat=True)
    all_days = [base + datetime.timedelta(days=x) for x in range(14)]
    holidays = Holiday.objects.all().values_list('date', flat=True)
    valid_days = [format_date_for_django_form(day) for day in all_days if
                  day.weekday() in valid_weekday and day not in holidays]
    return valid_days





class TypeReservationModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class reservation_without_badge(forms.Form):
    dates = forms.ChoiceField(choices=[], label="date", widget=forms.Select(attrs={'class': "form__select"}))

    def __init__(self, *args, **kwargs):
        super(reservation_without_badge, self).__init__()
        self.fields['dates'].choices = get_valid_days()

    def clean_dates(self):
        data = self.cleaned_data['dates']
        valid_dates = get_valid_days()
        if data in valid_dates:
            return data
        else:
            raise forms.ValidationError("Don't break my form")


class reservation_with_badge(forms.Form):
    dates = forms.ChoiceField(choices=[], label="Date",
                              widget=forms.Select(attrs={'class': "form__select"}))
    type_reservation = forms.ModelChoiceField(queryset=None, label="Type de réservation",
                                              widget=forms.Select(attrs={'class': "form__select"}))
    duration = forms.ModelChoiceField(queryset=None, label="Durée",
                                      widget=forms.Select(attrs={'class': "form__select"}))

    def __init__(self, machineID, *args, **kwargs):
        super(reservation_with_badge, self).__init__()
        reservationtype = Machine.objects.filter(id=machineID)
        for reservation in reservationtype:
            self.fields['type_reservation'].queryset = reservation.typeReservation.all()
        self.fields['duration'].queryset = Machine.objects.none()
        self.fields['dates'].choices = get_valid_days()

# machines.widget.attrs.update({'class': 'special'}) # Pour ajouter des class
