from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django import forms
from routine.models import Routine

def main(request):
    currentuser = request.session['username']
    routinelist = Routine.objects.filter(username=currentuser)
    return render(request, 'routine/main.html',
	{"currentuser": currentuser,
	 "routinelist": routinelist,
	})

def routine(request):
    return HttpResponse("routines go here")

def addroutine(request):
    return render(request, 'routine/newroutine.html',
	{"currentuser": request.session['username'],
	})

def routineadded(request):
    currentuser = request.session['username']
    rname = request.POST.get('routinename')
    length = request.POST.get('length')

    if rname == '':
	return HttpResponse("type a name for your routine")
    elif length == '':
	return HttpResponse("type a length for your routine")
    try:
	length = int(length)
        try:
            routinetest = Routine.objects.get(routinename=rname)
        except Routine.DoesNotExist:
            newroutine = Routine(routinename=rname, length=length, username=currentuser)
            newroutine.save()
            return main(request)
        except:
	    return HttpResponse("that routine already exists")
        if routinetest.username == currentuser:
	    return HttpResponse("that routine already exists")
    except:
	return HttpResponse("that isn't a length")
	
def addexcercise(request):
    return HttpResponse("add a new excercise")

