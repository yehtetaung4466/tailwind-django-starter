import os
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from newproject.settings import BASE_DIR

# Create your views here.
def index(req):
    t = loader.get_template('../templates/index.html')
    return HttpResponse(t.render(context={'name':'yehtet'}))