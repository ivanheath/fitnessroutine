from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __unicode__(self):
	return self.username
