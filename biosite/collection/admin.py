from django.contrib import admin
from .models import Category, Specimen



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}


@admin.register(Specimen)
class SpecimenAdmin(admin.ModelAdmin):
    list_display = ['category','common_name','botanical_name','created','slug']
    prepopulated_fields = {'slug':('common_name',)}
