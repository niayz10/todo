
from django.db import models
from django.utils import timezone

# Create your models here.


class ToDo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    todo_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Item(models.Model):
    todo = models.ForeignKey(ToDo, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(default="")
    item_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title