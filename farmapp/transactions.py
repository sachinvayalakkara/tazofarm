from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.http import JsonResponse
from django.core import serializers

# ////////cropmaintanance///////

def fn_showmanitanance(req):
    try:
        return render(req,'cropmaintanance.html')

    except Exception as e:
        print(e)

def fn_cropmainadd(req):
    try:
        return render(req,'cropmadd.html')

    except Exception as e:
        print(e)

