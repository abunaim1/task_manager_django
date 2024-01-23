from django.db import models
from category.models import Category
# Create your models here.

class Task(models.Model):
    taskTitle = models.CharField(max_length=100, verbose_name='Task Title')
    taskDescription = models.TextField()
    isCompleted = models.BooleanField(default=False)
    assignDate = models.DateTimeField()
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return self.taskTitle
    
    
