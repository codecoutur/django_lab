from django.db import models
class Student(models.Model):
    usn = models.CharField(max_length = 20,primary_key=True)
    name = models.CharField(max_length = 50)
    sem = models.IntegerField(default=6)
class Course(models.Model):
    course_code = models.CharField(max_length = 20,default="21CS61")
    course_name = models.CharField(max_length = 20)
    course_credits = models.IntegerField()
    students = models.ManyToManyField(Student,related_name = "student_course")
class Project(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    ptopic = models.CharField(max_length = 20)
    planguage = models.CharField(max_length = 30)
    pduration = models.IntegerField()
    
# Create your models here.
