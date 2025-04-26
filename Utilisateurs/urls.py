from django.urls import path
from .views import * 
from django.conf import settings
from django.conf.urls.static import static
from Utilisateurs.views import Verification_Mail

urlpatterns= [

    path("connecter/",connecter_compte, name='login'),
    path("creation/",Creation_compte, name='creation'),
    path("verification/",Verification_Mail, name='verification'),
    path("modification-code/<str:email>/", Changement_code, name='modifiercode'),





]