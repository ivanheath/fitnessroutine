from django.db import models

class Exercises(models.Model):
    exercisename = models.CharField(max_length=200)
    exercisedescription = models.CharField(max_length=400)
    musclegroup = models.CharField(max_length=200)

    def __unicode__(self):
        return self.exercisename

class Routine(models.Model):
    routinename = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    length = models.IntegerField(default=4)

    def __unicode__(self):
        return self.routinename

class Exercisespecific(models.Model):
    day = models.CharField(max_length=200)
    routine = models.ForeignKey(Routine)
    Exercise = models.ForeignKey(Exercises)

