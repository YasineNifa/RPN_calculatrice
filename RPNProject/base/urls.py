from django.urls import path
from .views import home, createStack, stack, deleteOperation, deleteStack

urlpatterns = [
    path('', home, name="home"),
    path('stack/', createStack, name="create-stack"),
    path('stack/<str:pk>', stack, name='stack'),
    path('delete-operation/<str:pk>/', deleteOperation, name='delete-operation'),
    path('delete-stack/<str:pk>/', deleteStack, name='delete-stack'),
]

