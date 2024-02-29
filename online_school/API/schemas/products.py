from ninja import ModelSchema, Schema
from ..models import Product
from ..schemas.users import UserSchema
from datetime import datetime

class ProductSchema(ModelSchema):
    creator: UserSchema
    num_lessons: int
    num_active_students: int
    purchase_percentage: float
    class Meta:
        model = Product
        fields = "__all__"


class CreateProductSchema(Schema):
    creator_id: int
    name: str
    start_datetime: datetime
    cost: float
    min_students: int
    max_students: int

class UpdateProductSchema(CreateProductSchema):
    ...



class CreateProductAccessSchema(Schema):
    user_id: int
    product_id: int
