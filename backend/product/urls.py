from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.CreateProductView.as_view()),
    path("create/category/", views.CreateCategoryView.as_view()),
    path("create/tag/", views.CreateTagView.as_view()),
]
