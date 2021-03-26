import os
from django.shortcuts import render, redirect

def index(request):
    context = {}
    return render(request, 'app/home.html', context)

def about(request):
    context = {}
    return render(request, 'app/aboutus.html', context)

def mycareplan(request):
    context = {}
    return render(request, 'app/mycareplan.html', context)

def mycareteam(request):
    context = {}
    return render(request, 'app/mycareteam.html', context) 

def contact(request):
    context = {}
    return render(request, 'app/contact.html', context)

def departments(request):
    context = {}
    return render(request, 'app/departments.html', context)

def doctors(request):
    context = {}
    return render(request, 'app/doctors.html', context)

def blogs(request):
    context = {}
    return render(request, 'app/blogs.html', context)

def today(request):
    context = {}
    return render(request, 'app/today.html', context)

def healthdata(request):
    context = {}
    return render(request, 'app/healthdata.html', context)

def sources(request):
    context = {}
    return render(request, 'app/sources.html', context) 

def department(request):
    context = {}
    return render(request, 'app/department.html', context)   

def departments(request):
    context = {}
    return render(request, 'app/departments.html', context)           