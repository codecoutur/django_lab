from django.urls import path
from . import views
urlpatterns = [
    path("cl/",views.cl, name = "cl"),
    path("sl/",views.sl, name = "sl"),
    path("el/",views.el, name ="e1"),
    path("reg/",views.reg,name = "reg"),
    path("preg/",views.projectreg,name = "projectreg"),
    path("pl/",views.pl,name = "pl")
]