from django.urls import path
from . import views

urlpatterns = [
    path("game/", views.game, name="game"),
    path('options/<int:category_id>/', views.options, name='options'),
]
