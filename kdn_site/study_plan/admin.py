from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'study_time')

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'study_time')

@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'study_time', 'planned_to_study', 'last_study')
