from django.shortcuts import render
from .models import Project

# Create your views here.
def Portfolio(request):
    projects = Project.objects.all()
    return render(request, "portfolio/Portfolio.html", {'projects' : projects})