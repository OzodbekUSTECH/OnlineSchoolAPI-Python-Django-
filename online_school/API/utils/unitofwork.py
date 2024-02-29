from typing import Type
from .. import repositories
from .. import models





class UnitOfWork:
    products: Type[repositories.ProductsRepository]
    product_access: Type[repositories.ProductAccessRepository]
    lessons: Type[repositories.LessonsRepository]
    groups: Type[repositories.GroupsRepository]


    def __enter__(self):
        self.products = repositories.ProductsRepository(model=models.Product)
        self.product_access = repositories.ProductAccessRepository(model=models.ProductAccess)
        self.lessons = repositories.LessonsRepository(model=models.Lesson)
        self.groups = repositories.GroupsRepository(model=models.Group)


    def __exit__(self, *args):
        return
    
    