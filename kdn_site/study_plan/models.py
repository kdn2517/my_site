from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')
    study_time = models.IntegerField(verbose_name='Время изучения')

    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование '
                                                                         'подкатегории')
    study_time = models.IntegerField(verbose_name='Время изучения')
    category = models.ForeignKey('Category', on_delete=models.PROTECT,
                                 verbose_name='Подкатегория')

    def __str__(self):
        return self.title

class Subjects(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    content = models.TextField(blank=True, verbose_name='Контент')
    planned_to_study = models.DateTimeField(auto_now_add=True, verbose_name='Дата начала')
    last_study = models.DateTimeField(auto_now=True, verbose_name='Последнее изучение')
    study_time = models.IntegerField(verbose_name='Время изучения')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Фото', blank=True,)
    studied = models.BooleanField(default=True, verbose_name='Изучено?')
    category = models.ForeignKey('SubCategory', on_delete=models.PROTECT,
                                 verbose_name='Подкатегория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['-planned_to_study']