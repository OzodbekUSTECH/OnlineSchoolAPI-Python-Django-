from ..schemas import groups as schema
from ..utils.unitofwork import UnitOfWork


class GroupsService:

    def create_group(
        self, uow: UnitOfWork, group_data: schema.CreateGroupSchema
    ):
        with uow:
            return uow.groups.create(group_data.model_dump())

    def get_groups(self, uow: UnitOfWork):
        with uow:
            return uow.groups.get_all()

    def get_group_by_id(self, uow: UnitOfWork, id: int):
        with uow:
            return uow.groups.get_by_id(id)

    def update_group(
        self, uow: UnitOfWork, id: int, group_data: schema.UpdateGroupSchema
    ):
        with uow:
            return uow.groups.update(id, group_data.model_dump())

    def delete_group(self, uow: UnitOfWork, id: int):
        with uow:
            return uow.groups.delete(id)
