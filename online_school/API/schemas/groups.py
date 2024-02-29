from os import name
from ninja import ModelSchema, Schema
from ..models import Group

class GroupSchema(ModelSchema):
    min_students: int
    max_students: int
    filled_percentage: float
    class Meta:
        model = Group
        fields = "__all__"
        


class CreateGroupSchema(Schema):
    product_id: int
    name: str
    

class UpdateGroupSchema(CreateGroupSchema):
    ...


