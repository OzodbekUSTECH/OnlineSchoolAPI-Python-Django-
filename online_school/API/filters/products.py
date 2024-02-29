from ninja import FilterSchema, Field
from typing import Optional


class ProductFilterSchema(FilterSchema):
    name: Optional[str] = Field(None, q='name__icontains')
    creator_name: Optional[str] = Field(None, q='creator__username__icontains') 