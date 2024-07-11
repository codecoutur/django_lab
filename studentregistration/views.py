from django.shortcuts import render
from .models import Student,Course,Project
from .forms import ProjectForm
from django.http import HttpResponse
#--------------------------------2C------------------------------------------------------
def sl(request):
    students = Student.objects.all()
    return render(request,"sl.html",{"students":students})
def cl(request):
    courses = Course.objects.all()
    return render(request,"cl.html",{"courses":courses})
def el(request):
    courses = Course.objects.all()
    if request.method == "POST":
        course_id = request.POST.get("course")
        courseobj = Course.objects.get(id = course_id)
        students = courseobj.students.all()
        return render(request,"el.html",{"courses":courses,"students":students})
    return render(request,"el.html",{"courses":courses})
def reg(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    if request.method == "POST":
        course_id = request.POST.get("course")
        student_usn = request.POST.get("student")
        
        courseobj = Course.objects.get(id = course_id)
        studentobj = Student.objects.get(usn = student_usn)
        if studentobj not in courseobj.students.all():
            result = f"student {studentobj.usn} is enrolled to course {courseobj.course_name}"
            courseobj.students.add(studentobj)
        else:
            result = f"student {studentobj.usn} has already enrolled to course {courseobj.course_name}"
        return render(request,"reg.html/",{"courses":courses,"students":students,"result":result})
    return render(request,"reg.html",{"courses":courses,"students":students})

#----------------------------------------3B----------------------------------
def projectreg(request):
    form = ProjectForm()
    if request.method == "POST":
        form_data = ProjectForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            result = "Record added successfully"
        else:
            result = "Record not added successfully"
        return render(request,"projectreg.html",{"form":form,"result":result})
    else:
       return render(request,"projectreg.html",{"form":form}) 
def pl(request):
    projects = Project.objects.all()
    if request.method == "POST":
        project_id = request.POST.get("project")
        projectobj = Project.objects.get(id = project_id)
        student = projectobj.student
        return render(request,"pl.html",{"projects":projects,"student":student})
    return render(request,"pl.html",{"projects":projects})

# Create your views here.
