from django.urls import path, include
from . import views

urlpatterns = [
    path("groups/",
        include(
        [
            path("", views.groups, name="groups"),
            path("detail/<int:id>/", views.detail, name="detail"),
            path("create/", views.create, name="create"),
            path("update/<int:id>/", views.update, name="update"),
            path("delete/<int:id>/", views.delete, name="delete"),
        ]
    ))
]