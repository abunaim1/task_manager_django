from django.db import models
# Create your models here.

class Category(models.Model):
    categoryName = models.CharField(max_length=100, verbose_name='Category Name')
    
    def __str__(self) -> str:
        return self.categoryName
    