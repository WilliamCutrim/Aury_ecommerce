from django.shortcuts import render
from django.views.generic import TemplateView, FormView

class IndexView(TemplateView):

    template_name = 'index.html'