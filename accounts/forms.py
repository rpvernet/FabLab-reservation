from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='Identifiant', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Mot de passe', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    first_name = forms.CharField(label='Prénom', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    last_name = forms.CharField(label='Nom de famille', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    username = forms.CharField(label='Identifiant', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    email = forms.EmailField(label='Courriel', max_length=100, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password = forms.CharField(label='Mot de passe', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    password_conf = forms.CharField(label='Confirmation de mot de passe', max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


