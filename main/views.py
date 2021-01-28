from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return HttpResponse("T           his is a <strong> bold </strong> song and this is done by Rupesh Dahal")# Create your views here.
