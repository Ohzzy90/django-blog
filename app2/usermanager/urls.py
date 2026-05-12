from django.urls import path
from .views import commentbox, del_comment, logout_request, reaction, register_user, login_request,profilemanager


urlpatterns=[
    path("register/",register_user, name="register"),
    path("login/",login_request, name="login"),
    path("logout/",logout_request, name="logout"),
    path("profile/",profilemanager, name="profile"),
    path("comment/<int:id>", commentbox, name="comment"),
    path("like/", reaction, name="like"),
    path("detail/comment/<int:id>", del_comment, name="del"),

    
]