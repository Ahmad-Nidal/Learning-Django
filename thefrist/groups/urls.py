
from django.urls import path
from . import views


urlpatterns = [
    path('groups/', views.groups, name='groups'),
    path('groups/detail/<int:id>/', views.detail, name='detail'),
    path('groups/create/', views.create, name='create'),
    path('groups/update/<int:id>/', views.update, name='update'),
    path('groups/delete/<int:id>/', views.delete, name='delete'),
]
