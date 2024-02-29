from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate,
    PageNumberPaginationExtra,
    PaginatedResponseSchema,
)

from ..schemas import products as schema
from ..services.products import ProductsService
from ..utils import permissions
from ..utils.unitofwork import UnitOfWork
from ..filters.products import ProductFilterSchema


@api_controller("/products", tags=["Products"])
class ProductsController:
    def __init__(self, products_service: ProductsService, uow: UnitOfWork):
        self.products_service = products_service
        self.uow = uow

    """
    Задание 1: Логика распределения
    *Добавил немного своей логики, т.к. не было уточнено условие,
    когда все группы будут заняты.
    Я решил просто создать автоматически новую группу с названием = продукту*
    """    
    @route.post('/{id}/access/{user_id}')
    def get_access_to_product_and_product(
        self,
        id: int,
        user_id: int
    ):
       return self.products_service.get_access_to_product_and_group(self.uow, id, user_id)


    """
    Задание 2: Список продуктов
    *Не уточнили какие продукты являются доступными для покупки :(
    поэтому решил выводить всё, что имеется*
    """    
    @route.get(
        "/", response=PaginatedResponseSchema[schema.ProductSchema]
    )
    @paginate(PageNumberPaginationExtra, page_size=50)
    def get_products(self, filters: ProductFilterSchema = Query(...)):
        products = self.products_service.get_products(self.uow)
        return filters.filter(products)


    """
    Убрал CRUD, т.к. в задание не сказано об этом, но он работает
    Оставил только нужное по задаче!
    """
    # @route.post("/", response=schema.ProductSchema)
    # def create_product(self, product_data: schema.CreateProductSchema):
    #     return self.products_service.create_product(self.uow, product_data)

    

    # @route.get(
    #     "/{id}",
    #     response=schema.ProductSchema,
    #     permissions=[permissions.HasAccessToProduct],
    # )
    # def get_product_by_id(self, id: int):
    #     return self.products_service.get_product_by_id(self.uow, id)

    # @route.put("/{id}", response=schema.ProductSchema)
    # def update_product(self, id: int, product_data: schema.UpdateProductSchema):
    #     return self.products_service.update_product(self.uow, id, product_data)

    # @route.delete("/{id}", response=schema.ProductSchema)
    # def delete_product(self, id: int):
    #     return self.products_service.delete_product(self.uow, id)