from os import access
from re import A
from django.shortcuts import render
from introduce.models import AccessLog

# Create your views here.
def introduce(request):
    access_log = AccessLog()
    access_log.locations ="introduce"
    access_log.save()
    
    return render(request, 'introduce.html')
