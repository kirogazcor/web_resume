# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone


class AboutMe(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=12)
    surname = models.CharField(verbose_name='Фамилия', max_length=12)
    about = models.TextField(verbose_name='Обо мне')
    birthday = models.DateField(verbose_name='Дата рождения')
    city = models.CharField(verbose_name='Город', max_length=12)
    suggestions = models.TextField(verbose_name='Условия')
    skills = models.TextField(verbose_name='Навыки')
    education = models.TextField(verbose_name='Образование')
    projects = models.TextField(verbose_name='Проекты')
    work = models.TextField(verbose_name='Опыт работы')

    class Meta:
        managed = False
        db_table = 'about_me'

class Education(models.Model):
    institution = models.CharField(verbose_name='Институт', max_length=64)
    qualification = models.CharField(verbose_name='Квалификация', max_length=12)
    specialty = models.CharField(verbose_name='Специальность', max_length=64)
    start = models.DateField(verbose_name='Начало')
    end = models.DateField(verbose_name='Окончание', default=timezone.now)
    description = models.TextField(verbose_name='Описание')
    site = models.CharField(verbose_name='Сайт', max_length=64)

    class Meta:
        managed = False
        db_table = 'education'

class Projects(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    description = models.TextField(verbose_name='Описание')
    realize = models.CharField(verbose_name='Реализация', max_length=32)
    git = models.CharField(verbose_name='Исходники', max_length=32)
    image = models.ImageField(verbose_name='Ссылка на картинку', max_length=32)

    class Meta:
        managed = False
        db_table = 'projects'

class Work(models.Model):
    organization = models.CharField(verbose_name='Организация', max_length=64)
    post = models.CharField(verbose_name='Должность', max_length=32)
    duties = models.TextField(verbose_name='Обязанности')
    start = models.DateField(verbose_name='Начало')
    end = models.DateField(verbose_name='Конец', default=timezone.now)

    class Meta:
            managed = False
            db_table = 'work'
