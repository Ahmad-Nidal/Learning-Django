
from django.urls import path
from . import views


urlpatterns = [
    path('groups/', views.groups, name='groups'),
    path('groups/group_detail/<int:group_id>/', views.group_detail, name='group_detail'),
]
