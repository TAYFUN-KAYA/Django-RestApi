from django.contrib import admin
from .models import Article,Writer,Student,School
# Register your models here.



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass


@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    pass


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    pass

