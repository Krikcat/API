from django.db import models

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login

class Sesion(models.Model):
    key = models.CharField(max_length=40)
    user = models.OneToOneField('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.key

class Cage(models.Model):
    id = models.AutoField(primary_key=True)


class Pets(models.Model):
    cage=models.ForeignKey('Cage', on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    sex_list = (('М','M'),('Ж','Ж'))
    sex = models.CharField(max_length=1,choices=sex_list)
    def __str__(self):
        return self.name