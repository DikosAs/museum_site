# Generated by Django 4.2.6 on 2023-10-17 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_front', '0002_contact_alter_objacts_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название сети')),
                ('url', models.CharField(max_length=128, verbose_name='Ссылка на сеть')),
                ('image', models.ImageField(upload_to='contacts/', verbose_name='Логотип сети')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
