from django.urls import path
from .views import * 

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Affichage.as_view(), name='home'),  # Garde seulement une seule route pour ""
    path('acc/', Acc, name='acc'),                # Change "acc" vers une URL propre
    path('ajout/', AjoutProduits.as_view(), name='ajout'),
    path('supprimer/<int:id>/', supprimer, name='supprimer'),  # Correction de "parg" en "path"
    #path('modification/<int:pk>/', update_donnees.as_view(), name='modifier'),
    path('detail/<int:pk>/', edit.as_view(), name='detail'),
    path('recherche/', recherche, name='recherche'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
