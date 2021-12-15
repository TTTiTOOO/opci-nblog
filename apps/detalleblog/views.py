from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from django.urls import reverse
from .models import Detalleblog

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from django import forms

# Create your views here
class DetallesBlog(ListView):
    model = Detalleblog
