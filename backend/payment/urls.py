from django.urls import path

from . import views


urlpatterns = [
    path("create/", views.CreatePaymentView.as_view()),
    path("read/<int:payment_id>/", views.ReadPaymentView.as_view()),
    path("delete/<int:payment_id>/", views.DeletePaymentView.as_view()),
]
