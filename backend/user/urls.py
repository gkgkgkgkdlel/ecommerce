from django.urls import path

from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view()),
    path("test/", views.TestView.as_view()),
]
