from django.db import models
from django.contrib import admin
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class Objacts(models.Model):
    # создаем столбец заголовков в нашей таблице
    title = models.CharField(verbose_name="Название предмета", max_length=128)
    # столбец - описание
    description = models.TextField(verbose_name="Описание предмета", null=True, default=None)
    # столбцы дат с автоматическим заполнением
    created_at = models.DateTimeField(verbose_name="Дата и время добавления предмета", auto_now_add=True) # автоматом при добавлении
    updated_at = models.DateTimeField(verbose_name="Дата и время обновления информации", auto_now=True) # автоматом при изменении

    image = models.ImageField(verbose_name="Изображение предмета", upload_to="objacts_img", default=None)

    @admin.display(description="Картинка")
    def show_image(self):
        from django.utils import html
        if self.image:
            return html.format_html("<img src='{}' style ='width:100px;'>", self.image.url)
        

class Contacts(models.Model):
    title = models.CharField(verbose_name="Название сети", max_length=128)
    url = models.CharField(verbose_name="Ссылка на сеть", max_length=128)
    image = models.ImageField(verbose_name="Логотип сети", upload_to="contacts")

    @admin.display(description="Картинка")
    def show_image(self):
        from django.utils import html
        if self.image:
            return html.format_html("<img src='{}' style ='width:100px;'>", self.image.url)