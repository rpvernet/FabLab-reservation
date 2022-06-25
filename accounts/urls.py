from django.urls import path

from . import views

urlpatterns = [
    path('connexion', views.login, name='login'),
    path('engregistrement', views.register, name='register'),
    path('deconnexion', views.logout, name='logout'),
    path('tableau_de_bord', views.dashboard, name='dashboard'),
    path('modidier', views.edit, name='edit'),
    path('modifier_mot_de_passe', views.change_password, name='change_password')
] 