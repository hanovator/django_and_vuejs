from django.urls import path
from . import views


app_name = 'todo'
urlpatterns = [
    path('vonly/', views.TodoVueOnlyTv.as_view(), name='vonly'),

    path('create/', views.TodoCV.as_view(), name='create'),
    path('lsit/', views.TodoLV.as_view(), name='list'),
    path('<int:pk>/delete/', views.TodoDelV.as_view(), name='delete'),

    path('mixin/', views.TodoMOMCV.as_view(), name='mixin'),
    path('<int:pk>/delete2/', views.TodoDelV2.as_view(), name='delete2'),
]
