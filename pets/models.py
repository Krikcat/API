from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    key = models.CharField(max_length=50)
    def __str__(self):
        return self.login

class Cage(models.Model):
    id = models.AutoField(primary_key=True)


class Pets(models.Model):
    cage=models.ForeignKey('Cage',null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=20)
    sex_list = (('М','M'),('Ж','Ж'))
    sex = models.CharField(max_length=1,choices=sex_list)
    def __str__(self):
        return self.name

