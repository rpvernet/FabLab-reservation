from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from accounts.FormValidation import FormValidation, FormValidationForEdit
from .forms import LoginForm, RegisterForm
from reservation.models import Reservation
from .models import Patron
import datetime
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.utils import timezone


def login(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        loginForm = LoginForm(request.POST)

        if loginForm.is_valid():

            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                messages.success(request, 'Vous êtes maintenant connecté')
                return redirect('dashboard')
            else:
                messages.error(request, 'Nom d\'utilisateur ou mot de passe invalide')
                return redirect('login')
    else:

        loginForm = LoginForm()

        return render(request, 'accounts/login.html',{ 'loginForm' : loginForm } )

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'Vous êtes maintenant déconnecté.')
        return redirect('login')

def register(request):

    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':

        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():

            first_name = registerForm.cleaned_data['first_name']
            last_name = registerForm.cleaned_data['last_name']
            username = registerForm.cleaned_data['username']
            email = registerForm.cleaned_data['email']
            password = registerForm.cleaned_data['password']
            password_conf = registerForm.cleaned_data['password_conf']

            validation = FormValidation(first_name, last_name, username, email, password, password_conf, request)

            validation.validate_register_form()

    else:

        registerForm = RegisterForm()

        return render(request, 'accounts/register.html',{ 'registerForm' : registerForm } )


    return render(request, 'accounts/register.html',{ 'registerForm' : registerForm } )

# FIXME: Les réservations du jour ne s'affichent pas.

def dashboard(request):

    if not request.user.is_authenticated:
        return redirect("register")

    reservations = Reservation.objects.filter(userID=request.user, starting_hours__gte=timezone.now()).order_by("starting_hours")
    user = User.objects.get(username=request.user)
    badge = Patron.objects.values('badges__badge_picture', 'badges__name').filter(user__username=request.user)

    context = { 'reservations' : reservations, 'patron': user, 'badges': badge}

    if request.method == 'POST':
        id = request.POST['id']

        reservation_to_delete = Reservation.objects.filter(id=int(id))


        send_mail(
			'Suppression réservation Fab Lab',
            'Ce message est pour vous confirmer l\'annulation de votre réservation le {} de {} à {}.'.format(reservation_to_delete[0].date.strftime("%d %B %Y"), reservation_to_delete[0].starting_hours.strftime("%H:%M"), reservation_to_delete[0].finishing_hours.strftime("%H:%M")),
			'fablab@brossard.ca',
			[request.user.email],
			fail_silently=False
				)

        reservation_to_delete.delete()
        messages.success(request, "Votre réservation a été supprimée")

    return render(request, 'accounts/dashboard.html', context)

def edit(request):

    if request.method == 'GET':
        user = User.objects.get(username=request.user)
        registerForm = RegisterForm(initial={'first_name': user.first_name, 'last_name': user.last_name,
                                         'username':user.username,'email': user.email, 'password': user.password})
        return render(request, 'accounts/edit.html', {'registerForm' : registerForm})

    if request.method == 'POST':

        registerForm = RegisterForm(request.POST)

        if registerForm.is_valid():

            first_name = registerForm.cleaned_data['first_name']
            last_name = registerForm.cleaned_data['last_name']
            username = registerForm.cleaned_data['username']
            email = registerForm.cleaned_data['email']

            validation = FormValidationForEdit(first_name, last_name, username, email, request)

            validation.validate_edit_form()


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Votre mot de passe a été modifié')
            return redirect('change_password')
        else:
            messages.error(request, 'Veuillez corriger les erreurs')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {
        'form': form
    })


