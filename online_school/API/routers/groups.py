from tokenize import group
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate,
    PageNumberPaginationExtra,
    PaginatedResponseSchema,
)
from ..schemas import groups as schema
from ..services.groups import GroupsService
from ..utils.unitofwork import UnitOfWork

@api_controller("/groups", tags=["Groups"])
class GroupsController:
    def __init__(self, groups_service: GroupsService, uow: UnitOfWork):
        self.groups_service = groups_service
        self.uow = uow

    #Доп задание: Насколько % заполненна группа
    @route.get('/', response=PaginatedResponseSchema[schema.GroupSchema])
    @paginate(PageNumberPaginationExtra, page_size=50)
    def get_groups(self):
        return self.groups_service.get_groups(self.uow)
    

    """
    Убрал CRUD, т.к. в задание не сказано об этом, но он работает
    Оставил только нужное по задаче!
    """
    # @route.post('/', response=schema.GroupSchema)
    # def create_group(self, group_data: schema.CreateGroupSchema):
    #     return self.groups_service.create_group(self.uow, group_data)
    
    
    # @route.get('/{id}', response=schema.GroupSchema)
    # def get_group_by_id(self, id: int):
    #     return self.groups_service.get_group_by_id(self.uow, id)

    
    # @route.put('/{id}', response=schema.GroupSchema)
    # def update_group(self, id: int, group_data: schema.UpdateGroupSchema):
    #     return self.groups_service.update_group(self.uow, id, group_data)
    
    # @route.delete('/{id}', response=schema.GroupSchema)
    # def delete_group(self, id: int):
    #     return self.groups_service.delete_group(self.uow, id)
    
