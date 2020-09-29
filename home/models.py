from django.db import models


# Create your models here.
class Todo(models.Model):
    pub_date = models.DateTimeField()
    text = models.TextField(max_length=300)
