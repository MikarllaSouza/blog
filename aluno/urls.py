from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("perfil/<int:id>/", views.perfil, name="perfil"),
]
