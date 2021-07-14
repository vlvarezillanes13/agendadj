from django.urls import path

from . import views

app_name = 'persona_app'

urlpatterns = [
    path(
        'personas/',
        views.ListaPersona.as_view(),
        name='personas'
    ),
    path(
        'api/persona/list/',
        views.PersonListApiView.as_view(),
    )
]
