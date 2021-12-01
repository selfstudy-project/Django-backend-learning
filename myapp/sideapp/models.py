from django.db import models

class Code(models.Model) :
    name = models.CharField(max_length=100,default='')
    code = models.CharField(max_length=500,default='')
