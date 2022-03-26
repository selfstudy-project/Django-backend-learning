from django.db import models

class Post(models.Model) :
    title = models.CharField(max_length = 100, default = '')
    content = models.CharField(max_length = 50000, default = '')
    tags = models.CharField(max_length = 100, default = '')
    author = models.CharField(max_length = 100, default =  '極速車神大佬')
    id = models.IntegerField(primary_key = True)
    hint = models.CharField(max_length = 100, default = '')