from ..schemas import products as schema, groups as groups_schema
from ..utils.unitofwork import UnitOfWork
from django.db.models import Count
from .. import models


class ProductsService:

    def create_product(
        self, uow: UnitOfWork, product_data: schema.CreateProductSchema
    ):
        with uow:
            return uow.products.create(product_data.model_dump())

    def get_products(self, uow: UnitOfWork):
        with uow:
            return uow.products.get_all()

    def get_product_by_id(self, uow: UnitOfWork, id: int):
        with uow:
            return uow.products.get_by_id(id)

    def update_product(
        self, uow: UnitOfWork, id: int, product_data: schema.UpdateProductSchema
    ):
        with uow:
            return uow.products.update(id, product_data.model_dump())

    def delete_product(self, uow: UnitOfWork, id: int):
        with uow:
            return uow.products.delete(id)
        

    # Получение доступа  и подключение клиента к группе(логика распределния)  
    def get_access_to_product_and_group(
            self, 
            uow: UnitOfWork, 
            id: int,
            user_id: int
        ):
        with uow:
            product: models.Product = uow.products.get_by_id(id)
            product_access: models.ProductAccess = uow.product_access.filter_by(product_id=id, user_id=user_id).first()

            # Создание доступа к продукту клиенту
            if not product_access:
                uow.product_access.create(schema.CreateProductAccessSchema(
                    user_id = user_id,
                    product_id = id
                ).model_dump())

                # Логика распределния в группу
                product_groups = uow.groups.filter_by(product=product.id).annotate(num_students=Count('students')).order_by('num_students')
                #Взяли группу с наименьшим числом студентов
                group_with_fewest_students: models.Group = product_groups.first()
                
                
                if product_groups and group_with_fewest_students.num_students < group_with_fewest_students.max_students:
                    # Добавляем пользователя в группу
                    group_with_fewest_students.students.add(user_id)
                    
                    selected_group = group_with_fewest_students
                else:
                    # Если группа уже достигла максимального количества студентов, создаем новую пустую группу с названием, как у продукта
                    group_data = groups_schema.CreateGroupSchema(
                        product_id = id,
                        name = product.name
                    )
                    new_group: models.Group = uow.groups.create(group_data.model_dump())
                    new_group.students.add(user_id)
                    selected_group = new_group
            else:
                # Если есть доступ, то вернем группу в которой находится пользователь относительно этого продукта
                selected_group = uow.groups.filter_by(product_id=id, students=user_id).first()

            return {"group_id": selected_group.id}
            


            

        
