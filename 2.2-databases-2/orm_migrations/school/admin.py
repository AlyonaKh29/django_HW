from django.contrib import admin

from .models import Student, Teacher


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['name', 'teachers', 'group']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    fields = ['name', 'subject']
