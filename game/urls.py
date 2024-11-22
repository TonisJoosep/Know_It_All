from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("game/", views.game, name="game"),
    path('options/<int:category_id>/', views.options, name='options'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
]
