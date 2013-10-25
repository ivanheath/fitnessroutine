from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django import forms
from routine.models import Routine, Exercises, Exercisespecific

def main(request):
    currentuser = request.session['username']
    routinelist = Routine.objects.filter(username=currentuser)
    return render(request, 'routine/main.html',
	{"currentuser": currentuser,
	 "routinelist": routinelist,
	})

def routine(request):
    request.session['currentroutine'] = request.get_full_path()[14:]
    routine = Routine.objects.get(routinename=request.session['currentroutine'])
    routinetime = routine.length + 1
    exerciselist = Exercisespecific.objects.filter(routine=routine)
    mondayexercise = Exercisespecific.objects.filter(routine=routine, day="monday")
    tuesdayexercise = Exercisespecific.objects.filter(routine=routine, day="tuesday")
    wednesdayexercise = Exercisespecific.objects.filter(routine=routine, day="wednesday")
    thursdayexercise = Exercisespecific.objects.filter(routine=routine, day="thursday")
    fridayexercise = Exercisespecific.objects.filter(routine=routine, day="friday")
    saturdayexercise = Exercisespecific.objects.filter(routine=routine, day="saturday")
    sundayexercise = Exercisespecific.objects.filter(routine=routine, day="sunday")
    test = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    return render(request, 'routine/routine.html',
	{"currentuser": request.session['username'],
	 "currentroutine": request.session['currentroutine'],
	 "routinelength": range(1, routinetime),
	 "routinetime": routinetime,
	 "exerciselist": exerciselist,
	 "mondayexercise": mondayexercise,
	 "tuesdayexercise": tuesdayexercise,
	 "wednesdayexercise": wednesdayexercise,
	 "thursdayexercise": thursdayexercise,
	 "fridayexercise": fridayexercise,
	 "saturdayexercise": saturdayexercise,
	 "sundayexercise": sundayexercise,
	 "test": test,
	})

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
	
def deleteroutine(request):
    routinetodelete = request.POST.get('deleteroutine')
    Routine.objects.get(routinename=routinetodelete).delete()
    return main(request)

def addexercise(request):
    routine = Routine.objects.get(routinename = request.session['currentroutine'])
    exerciselist = Exercises.objects.all()
    currentroutineexerciselist = Exercisespecific.objects.filter(routine=routine)
    return render(request, 'routine/addexercise.html',
	{"exerciselist": exerciselist,
	 "currentroutineexerciselist" : currentroutineexerciselist,
	})

def exerciseadded(request):
    option = request.POST.get('option')
    exercisename = request.POST.get('exercisename')
    day = request.POST.get('day')
    routine = Routine.objects.get(routinename=request.session['currentroutine'])
    if option == "addnew":
	exercisedescription = request.POST.get('exercisedescription')
        musclegroup = request.POST.get('musclegroup')
	if exercisename == '':
	    return HttpResponse("please type an exercise name")
	elif exercisedescription == '':
	    return HttpResponse("please type an exercise description")
	elif musclegroup == '':
	    return HttpResponse("please type a muscle group for the exercise")
	else:
	    try:
		Exercises.objects.get(exercisename=exercisename)
		return HttpResponse("that exercise allready exists")
	    except:
                newexercise = Exercises(exercisename=exercisename, exercisedescription=exercisedescription, musclegroup=musclegroup)
	        newexercise.save()
	        newexerciseS = Exercisespecific(day=day, routine=routine, Exercise=newexercise)
	        newexerciseS.save()
       
    elif option == "addlist":
	newexerciseS = Exercisespecific(day=day, routine=routine, Exercise=Exercises.objects.get(exercisename=exercisename))
	newexerciseS.save()

    elif option == "deletecurrent":
	split=exercisename.find(':')
	day = exercisename[split+1:]
	exercisename=exercisename[:split]
	Exercisespecific.objects.get(day=day, Exercise=Exercises.objects.get(exercisename=exercisename)).delete() 
 
    elif option == "deletedb":
	exercise = Exercises.objects.get(exercisename=exercisename)
	Exercisespecific.objects.filter(Exercise=exercise).delete()
	Exercises.objects.get(exercisename = exercisename).delete()
	

    return main(request)
