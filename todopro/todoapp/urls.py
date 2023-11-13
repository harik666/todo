from . import views
from django.urls import path

app_name = 'todoapp'

urlpatterns = [
    path('', views.fun_add1, name="show1"),
   # path('add', views.fun_add1, name="add1"),
    path('todo_det', views.fun_det3, name="todo_det1"),
    path('del/<int:taskID>/', views.fun_del, name="del1"),
    path('edit/<int:taskID>/', views.fun_edit, name="edit1"),
    path('lsTaskView/', views.lsView1.as_view(), name="lsView1"),
    path('dtTaskView/<int:pk>/', views.dtView1.as_view(), name="dtView1"),
    path('upTaskView/<int:pk>/', views.updat1.as_view(), name="updView1"),
    path('delTaskView/<int:pk>/', views.clsDel1.as_view(), name="delView1"),

]
