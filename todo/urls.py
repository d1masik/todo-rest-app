from django.urls import path
from todo import views


app_name = 'todo'

urlpatterns = [
    path('todo-list/', views.TodoViewSet.as_view({'get': 'list'}), name="todo-list"),
    path('todo-done/', views.TodoViewSet.as_view({'get': 'done'}), name="todo-list"),

    path('todo-detail/<str:pk>/', views.TodoViewSet.as_view({'get': 'retrieve'}), name="todo-detail"),
    path('todo-create/', views.TodoViewSet.as_view({'post': 'create'}), name="todo-create"),

    path('todo-update/<str:pk>/', views.TodoViewSet.as_view({'get': 'retrieve', 'post': 'update'}), name="todo-update"),
    path('todo-delete/<str:pk>/', views.TodoViewSet.as_view({'get': 'retrieve', 'post': 'destroy'}), name="todo-delete"),
]
