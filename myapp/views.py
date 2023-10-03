from django.shortcuts import render
from django.views.generic import TemplateView



class IndexView(TemplateView):
    template_name = 'index.html'



class IndexParticles(TemplateView):
    template_name = 'index-particles.html'


class IndexSlides(TemplateView):
    template_name = 'index-slides.html'


class IndexStatic(TemplateView):
    template_name = 'index-static.html'

