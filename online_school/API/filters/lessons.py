from ninja import FilterSchema, Field
from typing import Optional


class LessonsFilterSchema(FilterSchema):
    product_id: Optional[int] = Field(None)
    user_id: Optional[int] = Field(None, q='product__product_accesses__user_id')
