from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("여기는 홈이에요")

# Create your views here.
