from django.shortcuts import render
from django.views import generic

from .models import MainQuestion

# Create your views here.

class HomeView(generic.ListView):
    template_name = 'home/homepage.html'
    context_object_name = 'main_question'

    def get_queryset(self):
        return MainQuestion.objects.all()[0]