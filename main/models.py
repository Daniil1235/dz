import django
import os
from django.db import models


def phone_photo_path(instance, filename):
    if os.path.isfile("main/static/main/img/phones/none.jpg"):
        os.remove("main/static/main/img/phones/none.jpg")
    return f'main/static/main/img/phones/{instance.id}.jpg'


def producer_photo_path(instance, filename):
    if os.path.isfile("main/static/main/img/producer/none.jpg"):
        os.remove("main/static/main/img/producer/none.jpg")
    return f'main/static/main/img/producer/{instance.id}.jpg'


def category_photo_path(instance, filename):
    if os.path.isfile("main/static/main/img/category/none.jpg"):
        os.remove("main/static/main/img/category/none.jpg")
    return f'main/static/main/img/category/{instance.id}.jpg'


class Producer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание изготовителя')
    image = models.ImageField('Изображение компании', upload_to=producer_photo_path, blank=True)
    date = models.DateField('Дата регистрации на сайте', default=django.utils.timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'изготовитель'
        verbose_name_plural = 'изготовители'


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100)
    short_description = models.TextField('Краткое описание')
    image = models.ImageField('Изображение', upload_to=category_photo_path, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание и характеристики')
    color = models.CharField('Цвет', max_length=50)
    producer = models.ManyToManyField(Producer, verbose_name='Изготовители')
    category = models.ManyToManyField(Category, verbose_name='Категории', blank=True)
    image = models.ImageField('Изображение', upload_to=phone_photo_path, blank=True)
    price = models.FloatField('Цена')
    stock = models.BooleanField('В наличии', default=True)
    date = models.DateField('Дата выхода на продажу', default=django.utils.timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'телефон'
        verbose_name_plural = 'телефоны'
