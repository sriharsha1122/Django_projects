from django.urls import path
from .views import Tasklist , Taskdetail , Taskcreate ,Taskupdate ,Taskdelete ,CustomLoginView ,RegisterPage

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(next_page= 'login'),name='logout'),
    path('register/',RegisterPage.as_view(),name= 'register'),


    path('',Tasklist.as_view(),name='tasks'),
    path('task/<int:pk>/',Taskdetail.as_view(),name='task'),
    path('task-create/',Taskcreate.as_view(),name='task-create'),
    path('task-update/<int:pk>/',Taskupdate.as_view(),name='task-update'),
    path('task-delete/<int:pk>/',Taskdelete.as_view(),name='task-delete'),
]