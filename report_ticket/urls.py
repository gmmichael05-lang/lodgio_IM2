from django.urls import path
from . import views

urlpatterns = [

 path('reports/', views.report_list, name='report_list'),
    path('reports/add/', views.report_add, name='report_add'),
]