from django.db import models

class admins(models.Model):
    username=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    password=models.CharField(max_length=30)

    def __str__(self):
        return self.username

class students(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    semister=models.CharField(max_length=30)
    school = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class courses(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    course=models.CharField(max_length=30)
    faculty = models.CharField(max_length=30)
    fee = models.CharField(max_length=30)

    def __str__(self):
        return self.name

