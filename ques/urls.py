from django.urls import path
from . import views

urlpatterns = [
    path('', views.askquestion, name='askquestion'),
]