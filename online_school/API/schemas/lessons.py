from ninja import ModelSchema, Schema
from ..models import Lesson

class LessonSchema(ModelSchema):
    class Meta:
        model = Lesson
        fields = "__all__"


class CreateLessonSchema(Schema):
    product_id: int
    title: str
    video_link: str

class UpdateLessonSchema(CreateLessonSchema):
    ...