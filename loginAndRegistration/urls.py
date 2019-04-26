from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserView)

urlpatterns = [
    path('', views.index, name="index"),
    path('success', views.success, name="success"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('apiroot', include(router.urls)),
]