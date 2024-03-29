from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.Upload_Task, name='upload'),
    path('update/<int:pk>', views.Update_Task, name='update'),
    path('delete/<int:pk>', views.Delete_Task, name='delete'),

]
