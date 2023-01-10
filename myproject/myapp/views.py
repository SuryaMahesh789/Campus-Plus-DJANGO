
from django.shortcuts import render

from django.http import HttpResponse

from .models import *

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def registeradmin(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    obj = admins(username=username, email=email, password=password)
    obj.save()
    return render(request, "index.html")

def checkadmin(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    l = admins.objects.filter(username=username, email=email, password=password)

    if(len(l)>0):
        message = "Authenticated User..."
        return render(request, "index.html")
    else:
        message = "User Not Found In Records..Register/Enter Details Correctly"
        return render(request, "login.html")

def addpage(request):
    return render(request,'addpage.html')

def removepage(request):
    return render(request,'removepage.html',{"message":""})

def searchpage(request):
    return render(request,'searchpage.html')

def displaypage(request):
    l = students.objects.all()
    return render(request,'displaypage.html',{"l":l})

def showpage(request):
    l=admins.objects.all()
    return  render(request,'showpage.html',{'l':l})


def index(request):
    return render(request,'index.html')

def addpage(request):
    return render(request,'addpage.html',{"message":""})

def addstudent(request):
    name = request.POST['name']
    email = request.POST['email']
    semister = request.POST['semister']
    school = request.POST['school']
    address = request.POST['address']
    city = request.POST['city']

    obj = students(name=name, email=email, semister=semister, school=school,address=address,city=city)
    obj.save()

    return render(request,'addpage.html',{"message":"ADDED SUCCESSFULLY...."})

def deladmin(request):
    return render(request, 'removeadmin.html',{"message":""})


def removeadmin(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    l = admins.objects.filter(username=username, email=email, password=password)
    if(len(l)>0):
        l = admins.objects.get(username=username, email=email, password=password)
        l.delete()
        return render(request, 'removeadmin.html',{"message":"Admin Dropped Successfully...."})
    else:
        return render(request, 'removeadmin.html', {"message": "No Results Found... "})

def removestudent(request):
    name = request.POST['name']
    email = request.POST['email']
    l = students.objects.filter(name=name, email=email)
    if(len(l)>0):
        l = students.objects.get(name=name, email=email)
        l.delete()
        return render(request, 'removepage.html',{"message":"Student Dropped Successfully...."})
    else:
        return render(request, 'removepage.html', {"message": "No Results Found... "})


def searchstudent(request):
    name = request.POST['name']
    email = request.POST['email']
    l = students.objects.filter(name=name, email=email)
    if (len(l) > 0):
        l = students.objects.get(name=name, email=email)
        return render(request, 'searchpage.html', {"message":"Student Found In The Records...","l":l})
    else:
        return render(request, 'searchpage.html', {"message":"Student Not Found In The Records..."})


def manage(request):
    return render(request,'managestudent.html')

def managestudent(request):
    name = request.POST['name']
    email = request.POST['email']
    course = request.POST['course']
    faculty = request.POST['faculty']
    fee = request.POST['fee']
    l = students.objects.filter(name=name, email=email)
    if (len(l) > 0):
        obj = courses(name=name, email=email, course=course, faculty=faculty, fee=fee)
        obj.save()
        return render(request, 'managestudent.html', {"message": "COURSE ALLOTED TO THE STUDENT..."})
    else:
        return render(request, 'managestudent.html', {"message": "UNSUCCESSFUL ALLOTMENT -> STUDENT NOT FOUND IN RECORDS.."})


def coursedetails(request):
    l = courses.objects.all()
    return render(request,'coursedetails.html',{"l":l})
