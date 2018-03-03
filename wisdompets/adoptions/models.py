from django.db import models

class Pet(models.Model):
    
    SEX_CHOICE = [('M','Male'),('F','Female')]
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    description = models.TextField()
    sex = models.CharField(choices=SEX_CHOICE, max_length=1)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField('vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

