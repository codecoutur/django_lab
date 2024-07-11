#-------------------------------3A-------------------------------------------
from django.contrib import admin
from .models import Student,Course
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    model = Student
    list_display = ['usn','name','sem']
    ordering = ['usn']
    search_fields = ['usn']
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ['course_name','course_code','course_credits']
    ordering = ['course_code']
    search_fields = ['course_code']

# Register your models here.
