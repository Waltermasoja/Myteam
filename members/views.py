from django.shortcuts import render
from django.http import HttpResponse
from .models import Members

def index(request):
    return render(request,"home.html")

def members(request):
    mymembers = Members.objects.all().values()
    context = {
        'mymembers' :mymembers
    }
    return render(request,"all_members.html",context)
