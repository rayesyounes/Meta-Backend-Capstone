from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('api/token/login', TokenObtainPairView.as_view()),
    path('api/token/refresh', TokenRefreshView.as_view()),
]
