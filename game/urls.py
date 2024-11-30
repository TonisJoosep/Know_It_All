from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path("game/", views.game, name="game"),
    path('options/<str:category_name>/', views.options, name='options'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('privacy', views.privacy, name='privacy'),
    path('signup/' , views.signup, name='signup'),
    path('save-score/', views.save_score, name='save_score'),
    path('high_score/', views.high_score, name='high_score'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]
