from django.urls import path
from . import views
urlpatterns=[
    path("index/",views.displayList,name = "displayList"),
    path("home/",views.home, name = "home"),
    path("contact/",views.contact, name = 'contact'),
    path("about/",views.about,name = "about"),
]