from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    path("update/<int:pk>", views.update, name="word_card_update"),
    path("update/", views.update, name="word_card_create"),
    # ex: /polls/5/
    path("detail/<int:pk>", views.detail, name="word_card_detail"),
    # ex: /polls/5/vote/
    path("delete/<int:pk>", views.delete, name="word_card_delete"),
]