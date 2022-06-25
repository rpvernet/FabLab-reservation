from django.test import TestCase
from reservation.models import Reservation
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.FormValidation import FormValidation, FormValidationForEdit
from .forms import LoginForm, RegisterForm
from reservation.models import Reservation
from .models import Patron
from machines.models import Machine
from datetime import datetime, timezone
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.utils import timezone



# Create your tests here.
print(Machine.objects.values_list('context_without_badge', 'name').get(id=6))