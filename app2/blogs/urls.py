from django.urls import path
from .views import index,Post,DetailPost, EditDetails, deletepost

urlpatterns=[
    path("",index, name="Home"),
    path("addpost/",Post, name="addpost"),
    path("details/<int:id>/", DetailPost, name="details"),
    path("edit/<int:id>/",EditDetails , name="edit"),
    path("delete/<int:id>/", deletepost, name="delete")
]