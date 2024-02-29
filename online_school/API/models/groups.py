from django.db import models
from django.contrib.auth.models import User
from .products import Product

class Group(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Продукт, к которому относится группа
    name = models.CharField(max_length=100)  # Название группы
    students = models.ManyToManyField(User)  # Ученики группы

    @property
    def min_students(self):
        return self.product.min_students
    
    @property
    def max_students(self):
        return self.product.max_students
    
    @property
    def filled_percentage(self):
        num_students = self.students.count()
        max_students = self.max_students
       
        return round((num_students / max_students) * 100, 1)
    

    def __str__(self):
        return f"{self.id}. {self.name}"

   
    

    