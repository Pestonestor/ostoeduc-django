from datetime import datetime
from multiprocessing import context
from re import template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import loader
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'app1/publica/index.html')
