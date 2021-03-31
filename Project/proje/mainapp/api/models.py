from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=100,blank=True)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    


class Writer(models.Model):
    name = models.CharField(max_length=100,blank=True)
    phone_number = models.IntegerField()

    


class School(models.Model):

    name = models.CharField(max_length=100,blank=True)
    adress = models.TextField(blank=True, null=True)

    


class Student(models.Model):

    name = models.CharField(max_length=100,blank=True)
    surname = models.CharField(max_length=100)
    number = models.IntegerField()

    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    
