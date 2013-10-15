from django.db import models

class Excercises(models.Model):
    excercisename = models.CharField(max_length=200)
    excercisedescription = models.CharField(max_length=400)
    musclegroup = models.CharField(max_length=200)

    def __unicode__(self):
        return self.excercisename

class Routine(models.Model):
    routinename = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    length = models.IntegerField(default=4)

    def __unicode__(self):
        return self.routinename

class Excercisespecific(models.Model):
    day = models.CharField(max_length=200)
    routine = models.ForeignKey(Routine)
    Excercise = models.ForeignKey(Excercises)

