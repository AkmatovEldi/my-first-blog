from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        """
        Переопределяем метод сохранения модели
        """

        if not change:  # Проверяем что запись только создаётся
            obj.author = request.user  # Присваеваем полю автор текущего пользователя

        super(PostAdmin, self).save_model(
            request=request,
            obj=obj,
            form=form,
            change=change
        )