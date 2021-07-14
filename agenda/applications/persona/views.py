from django.shortcuts import render

from django.views.generic import ListView

from .models import Person

class ListaPersona(ListView):
    model = Person
    template_name = "persona/personas.html"
    context_object_name = 'personas'

    def get_queryset(self):
        return Person.objects.all()



