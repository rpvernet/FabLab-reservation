from django.contrib import messages, auth
from django.shortcuts import redirect
from django.contrib.auth.models import User
import re


#TODO: Retravailler la class pour permettre des arguments optionnels pour ne pas surcharger le création d'un objet pour les prochaines validations de formulaire

class FormValidation:
    def __init__(self, first_name, last_name, username, email, password, password_conf, request):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.password_conf = password_conf
        self.request = request

    def validate_register_form(self):

        # Prénom
        if not self.first_name:
            messages.error(self.request, 'Le prénom ne doit pas être vide')
            return redirect('register')
        elif len(self.first_name) < 3:
            messages.error(self.request, 'Le prénom doit être d\'au moins 3 caractères')
            return redirect('register')

        # Nom de famille

        if not self.last_name:
            messages.error(self.request, 'Le nom de famille ne doit pas être vide')
            return redirect('register')
        elif len(self.last_name) < 3:
            messages.error(self.request, 'Le nom de famille doit être d\'au moins 3 caractères')
            return redirect('register')

        # username

        if not self.username:
            messages.error(self.request, 'L\'identifiant ne doit pas être vide')
            return redirect('register')
        elif len(self.username) < 5:
            messages.error(self.request, 'L\'identifiant doit être d\'au moins 5 caractères')
            return redirect('register')
        elif User.objects.filter(username=self.username).exists():
            messages.error(self.request, 'Désolé, cet identifiant est déjà associé à un compte.')
            return redirect('register')

        # email
        
        if not self.email:
            messages.error(self.request, 'L\'adresse courriel doit être valide.')
            return redirect('register')
        elif re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', self.email) != None:
            messages.error(self.request, 'L\'adresse courriel doit être valide.')
            return redirect('register')
        elif User.objects.filter(email=self.email).exists():
            messages.error(self.request, 'Désolé, ce courriel est déjà associé à un compte.')
            return redirect('register')

        # Mot de passe

        if not self.password:
            messages.error(self.request, 'Le mot de passe ne doit pas être vide.')
            return redirect('register')
        elif len(self.password) < 6:
            messages.error(self.request, 'Le mot de passe doit être d\'au moins 8 caractères')
            return redirect('register')
        
        # Confirmation mot de passe

        if self.password_conf != self.password:
            messages.error(self.request, 'La confirmation du mot de passe doit être identique au mot de passe')
            return redirect('register')
        
        else:
            user = User.objects.create_user(username=self.username, password=self.password,email=self.email, first_name=self.first_name, last_name=self.last_name)

            user.save()
            user_to_connect = auth.authenticate(username=self.username, password=self.password)
            auth.login(self.request, user_to_connect)
            messages.success(self.request, 'Votre compte est maintenant activé.')
            return redirect('dashboard') # FIXME: La redirection ne fonctionne pas. L'utilisateur activé est dirigé vers la page register


class FormValidationForEdit:
    def __init__(self, first_name, last_name, username, email, request):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.request = request

    def validate_edit_form(self):

        # Prénom
        if not self.first_name:
            messages.error(self.request, 'Le prénom ne doit pas être vide')
            return redirect('register')
        elif len(self.first_name) < 3:
            messages.error(self.request, 'Le prénom doit être d\'au moins 3 caractères')
            return redirect('register')

        # Nom de famille

        if not self.last_name:
            messages.error(self.request, 'Le nom de famille ne doit pas être vide')
            return redirect('register')
        elif len(self.last_name) < 3:
            messages.error(self.request, 'Le nom de famille doit être d\'au moins 3 caractères')
            return redirect('register')

        # username

        if not self.username:
            messages.error(self.request, 'L\'identifiant ne doit pas être vide')
            return redirect('register')
        elif len(self.username) < 5:
            messages.error(self.request, 'L\'identifiant doit être d\'au moins 5 caractères')
            return redirect('register')
        elif User.objects.filter(username=self.username).exists():
            messages.error(self.request, 'Désolé, cet identifiant est déjà associé à un compte.')
            return redirect('register')

        # email

        if len(self.email) > 6:
            if re.match('\b[\w\.-]+@[\w\.-]+\.\w{2,4}\b', self.email) != None:
                messages.error(self.request, 'L\'adresse courriel doit être valide.')
                return redirect('register')
            elif User.objects.filter(email=self.email).exists():
                messages.error(self.request, 'Désolé, ce courriel est déjà associé à un compte.')
                return redirect('register')



        else:
            user = User.objects.update(username=self.username, email=self.email,
                                            first_name=self.first_name, last_name=self.last_name)

            user.save()
            messages.success(self.request, 'Vos informations sont à jour')
            return redirect('dashboard')