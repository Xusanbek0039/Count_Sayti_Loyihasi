from django.urls import path
from .views import *

urlpatterns = [
    path('',IndexView.as_view(),name='index'),
    path('indexslides/',IndexSlides.as_view(),name='index_slides'),
    path('index-particles/',IndexParticles.as_view(), name='index_particles'),
    path('index-static/',IndexStatic.as_view(), name='index_static'),
    ]