from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # Создатель продукта
    name = models.CharField(max_length=100)  # Название продукта
    start_datetime = models.DateTimeField()  # Дата и время старта продукта
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Стоимость продукта
    min_students = models.PositiveIntegerField()  # Минимальное количество участников в группе
    max_students = models.PositiveIntegerField()  # Максимальное количество участников в группе

    @property
    def num_lessons(self):
        return self.lessons.count()
    
    @property
    def num_active_students(self):
        return self.product_accesses.count()
    
    @property #Доп. Задание: Процент приобретения продукта
    def purchase_percentage(self):
        total_users_count = User.objects.exclude(id=self.creator_id).count()
        product_access_count = self.product_accesses.count()
        return round((product_access_count / total_users_count) * 100, 1)
    
    def __str__(self):
        return f"{self.id}. {self.name}"

class ProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_accesses')

    def __str__(self):
        return f"Студент: {self.user.id}. {self.user.username} - Продукт: {self.product.id}. {self.product.name}"