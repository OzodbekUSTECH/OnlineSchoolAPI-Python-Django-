from ninja import Query
from ninja_extra import api_controller, route
from ninja_extra.pagination import (
    paginate,
    PageNumberPaginationExtra,
    PaginatedResponseSchema,
)

from ..filters.lessons import LessonsFilterSchema
from ..schemas import lessons as schema
from ..services.lessons import LessonsService
from ..utils.unitofwork import UnitOfWork

@api_controller("/lessons", tags=["Lessons"])
class LessonsController:
    def __init__(self, lessons_service: LessonsService, uow: UnitOfWork):
        self.lessons_service = lessons_service
        self.uow = uow


    """
    Задача 3: Выведение списка уроков по конкретному продукту
    к которому пользователь имеет доступ
    """
    @route.get("/", response=PaginatedResponseSchema[schema.LessonSchema])
    @paginate(PageNumberPaginationExtra, page_size=50)
    def get_lessons(self, filters: LessonsFilterSchema = Query(...)):
        """
        + product_id - получить все уроки конкретно по этому продукту
        + user_id - Выдает уроки по конкретному продукту к которому есть доступ у клиента\n
                    !!! Если пустой results => нет доступа к продукту/нет уроков в продукте
        """
        lessons = self.lessons_service.get_lessons(self.uow)
        return filters.filter(lessons)


    

    """
    Убрал CRUD, т.к. в задание не сказано об этом, но он работает
    Оставил только нужное по задаче!
    """
    # @route.post("/", response=schema.LessonSchema)
    # def create_lesson(self, lesson_data: schema.CreateLessonSchema):
    #     return self.lessons_service.create_lesson(self.uow, lesson_data)

    
    # @route.get("/{id}", response=schema.LessonSchema)
    # def get_lesson_by_id(self, id: int):
    #     return self.lessons_service.get_lesson_by_id(self.uow, id)

    # @route.put("/{id}", response=schema.LessonSchema)
    # def update_lesson(self, id: int, lesson_data: schema.UpdateLessonSchema):
    #     return self.lessons_service.update_lesson(self.uow, id, lesson_data)
    
    # @route.delete('/{id}', response=schema.LessonSchema)
    # def delete_lesson(self, id: int):
    #     return self.lessons_service.delete_lesson(self.uow, id)