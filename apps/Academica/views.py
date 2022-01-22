from django.http import HttpResponse
from django.template import Template,Context
from django.template.loader import get_template
from django.shortcuts import render

import datetime


def inicio(request): #funcion vista
    return render(request, "base.html")
