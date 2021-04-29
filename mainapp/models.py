from django.db import models


# Create your models here.

class portfolio_project(models.Model):
    img_project = models.ImageField(
            upload_to='products_images',
            blank=True
    )
    name_project = models.CharField(
            verbose_name='Название проекта',
            max_length=13,
            unique=True
    )
    discription_project = models.CharField(
            verbose_name='Каткое описание',
            max_length=40,
            blank=True
    )
    platform = models.CharField(
            verbose_name='Название платформы',
            max_length=20
    )
    img_platform = models.ImageField(
            upload_to='products_images',
            blank=True
    )

    def __str__(self):
        return self.name_project


class career_path(models.Model):
    img_career = models.ImageField(
            upload_to='products_images',
            blank=True
    )
    date = models.PositiveIntegerField(
            verbose_name='Год трудоустройства'
    )
    name_info = models.CharField(
            verbose_name='Имя организации',
            max_length=44
    )
    discription_info = models.TextField(
            verbose_name='Каткое описание организации',
            blank=True
    )

    def __str__(self):
        return self.name_info
