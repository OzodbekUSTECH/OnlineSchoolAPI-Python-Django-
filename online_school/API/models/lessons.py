from django.db import models
from .products import Product

class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')  # Продукт, к которому относится урок
    title = models.CharField(max_length=100)  # Название урока
    video_link = models.URLField()  # Ссылка на видео урока

    def __str__(self):
        return f"{self.id}. {self.title}"