from django.db import models

class Pet(models.model):
    
    SEX_CHOICE = [('M','Male'),('F','Female')]

    name = models.chartField(max_lengh=100)

    submitter = models.chartField(max_lengh=100)

    species = models.chartField(max_lengh=30)

    breed = models.chartField(max_lengh=30)

    description = models.chartField()
    
    sex = models.chartField(choice=SEX_CHOICE, max_lengh=1)
