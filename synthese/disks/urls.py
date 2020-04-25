from django.urls import path
from . import views

urlpatterns = [
    path('<int:id_album>', views.album, name="album")
]