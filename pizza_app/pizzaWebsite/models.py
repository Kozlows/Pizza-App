from django.db import models

# Create your models here.
# EVERY TIME YOU MODIFY THIS FILE YOU HAVE TO MIGRATE YOUR DATABASE
# run these two commans 
# python manage.py makemigraions
# python manage.py migrate

class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
