from ..models import ProductAccess
from ninja_extra.permissions.base import BasePermission
from typing import TYPE_CHECKING
from django.http import HttpRequest
if TYPE_CHECKING:
    from ninja_extra.controllers.base import ControllerBase  # pragma: no cover


class HasAccessToProduct(BasePermission):

    def has_permission(
        self, request: HttpRequest, controller: "ControllerBase"
    ) -> bool:
        user = request.user
        
        # Проверяем, авторизован ли пользователь
        if not user.is_authenticated:
            return False

        # Получаем идентификатор продукта из запроса
        product_id = controller.context.kwargs.get('id')

        # Проверяем, существует ли запись ProductAccess для данного пользователя и продукта
        access_exists = ProductAccess.objects.filter(user=user, product_id=product_id).exists()

        return access_exists