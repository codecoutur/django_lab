from django.shortcuts import render
#--------------------------------------2A----------------------------------
def displayList(request):
    fruits = ["Apple","Orange","Pineapple","Bannana","groundnut"]
    students = ["Kajal","Pooja","Nanditha","Kajol","Navya"]
    return render(request,"index.html",{'fruits':fruits,'students':students})
#----------------------------------2B----------------------------------------
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
# Create your views here.
