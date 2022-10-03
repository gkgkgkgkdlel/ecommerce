from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.CreateOrderView.as_view()),
    path("read/<int:order_id>/", views.ReadOrderView.as_view()),
    path("read/detail/<int:order_id>/", views.ReadOrderDetailView.as_view()),
]
