
from django.urls import path
from . import views


urlpatterns = [
    path('groups/', views.groups, name='groups'),
    path('groups/details/<int:id>/', views.details, name='details'),
    path('groups/create/', views.create, name='create'),
    path('groups/update/<int:id>/', views.update, name='update'),
    path('groups/delete/<int:id>/', views.delete, name='delete'),
]
