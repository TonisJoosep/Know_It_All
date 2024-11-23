"""
URL configuration for know_it_all project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


from game import views

urlpatterns = [
    path('', include('game.urls')),
    path('admin/', admin.site.urls),

    path('options/<str:category_name>/', views.options, name='options'),
    path('forgot_password', views.forgot_password, name='forgot_password'),
    path('register/', views.register, name='register'),
    path('signup/', views.signup, name='signup'),
]
