from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django import forms
from login.models import Users
from routine.views import main

def login(request):
    request.session['username'] = ''
    return render(request, 'login/login.html')

def logincheck(request):
    user=request.POST.get('loginname')
    passw=request.POST.get('password')
    if user == '' or passw == '':
	return HttpResponse('username or password is blank')
    else:
	pass
    try:
        currentuser = Users.objects.get(username=user)
	if currentuser.password == passw:
	    request.session['username'] = currentuser.username
	    return main(request)
	    
	else:
	    return HttpResponse("username or password is invalid you foo")
    except:
	return HttpResponse('username or password is invalid')

def newuser(request):
    return render(request, 'login/newuser.html')

def useradded(request):
    uname = request.POST.get('username')
    pword = request.POST.get('password')
    pword2 = request.POST.get('password2')
    if uname == '' or pword == '' or pword2 == '':
	return HttpResponse('please fill in all fields')
    else:
	try:
	    currentuser = Users.objects.get(username=uname)
	except:
    	    if pword == pword2:
		addnewuser = Users(username=uname, password=pword)
		addnewuser.save()
		return render(request, 'login/useradded.html',
	    	    {"username": uname,
	    	    "password": pword,
	    	    "worked": "yes",
	    	    })
    	    else:
		return HttpResponse("your passwords don't match")
	return HttpResponse("that username already exists")
