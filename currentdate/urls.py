from django.urls import path
from . import views
urlpatterns = [
    path('cdt/',views.currentDate,name = "currentDate"),
    path('fha/',views.fourHoursAhead,name = "fourHoursAhead"),
    path('fhb/',views.fourHoursBefore,name = "fourHoursBefore"),
]