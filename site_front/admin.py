from django.contrib import admin
from .models import * # импортируем модель для работы с БД
# Register your models here.

# класс для управления моделью из админки
class ObjactsAdmin(admin.ModelAdmin):
    # столбцы, которые будут отображаться
    list_display = ["id", "title", "description", "image", "show_image", "updated_at", "created_at"]
    # кaстомизация полей ввода
    # fieldsets = (
    #     ("Общее", { # подзаголовок
    #         "fields": ("title", "description", "image") # поля внутри него
    #     })
    #     # ("Финансы", { # подзаголовок
    #     #     "fields": ("price", "auction"), # поля внутри него
    #     #     "classes": ["collapse"] # добавление класса (дизайна) для сворачивания и разворачивания
    #     # })
    # )

    # создаем действие, которое можно произвести с строчкой в таблице

class ContactsAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "url", "image", "show_image"]

# соединяем класс и модель
admin.site.register(Objacts, ObjactsAdmin)
admin.site.register(Contacts, ContactsAdmin)