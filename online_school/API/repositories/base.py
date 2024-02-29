from django.db import models
from ..utils.exceptions import Exceptions

class BaseRepository:
    def __init__(self, model: models.Model):
        self.model = model

    def create(self, data: dict):
        return self.model.objects.create(**data)

    def get_all(self):
        return self.model.objects.all()
    
    def get_by_id(self, id: int):
        try: 
            return self.model.objects.get(id=id)
        except:
            raise Exceptions.not_found("Invalid id")
            
        
    
    def update(self, id: int, data: dict):
        try:
            instance = self.model.objects.get(id=id)  # Use .first() to get the instance instead of a queryset
        except:
            raise Exceptions.not_found("Invalid id")
        
        for key, value in data.items():
            setattr(instance, key, value)

        instance.save()
        
        return instance
    
    def delete(self, id: int):
        try:
            instance = self.model.objects.get(id=id)
        except:
            raise Exceptions.not_found("Invalid id")

        instance.delete()
        return instance
        

    def filter_by(self, **kwargs):
        """
        Возвращает объекты модели, удовлетворяющие переданным фильтрам.
        :param kwargs: фильтры для запроса
        :return: QuerySet объектов модели
        """
        return self.model.objects.filter(**kwargs)
    