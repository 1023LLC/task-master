from django.urls import path
from . import views

app_name = 'task'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/delete_task/', views.delete, name='delete_task')
]