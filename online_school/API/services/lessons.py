from ..schemas import lessons as schema
from ..utils.unitofwork import UnitOfWork


class LessonsService:

    def create_lesson(
        self, uow: UnitOfWork, lesson_data: schema.CreateLessonSchema
    ):
        with uow:
            return uow.lessons.create(lesson_data.model_dump())

    def get_lessons(self, uow: UnitOfWork):
        with uow:
            return uow.lessons.get_all()

    def get_lesson_by_id(self, uow: UnitOfWork, id: int):
        with uow:
            return uow.lessons.get_by_id(id)

    def update_lesson(
        self, uow: UnitOfWork, id: int, lesson_data: schema.UpdateLessonSchema
    ):
        with uow:
            return uow.lessons.update(id, lesson_data.model_dump())

    def delete_lesson(self, uow: UnitOfWork, id: int):
        with uow:
            return uow.lessons.delete(id)
