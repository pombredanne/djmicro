from django.db import models
from django.forms import ModelForm

class Task(models.Model):
    title = models.CharField(max_length=255)

class TaskForm(ModelForm):
    class Meta:
        model = Task
