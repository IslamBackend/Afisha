from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.register),
    path('confrim/', views.confirm_code),
    path('login/', views.login),
    path('profile/', views.profile),
    path('logout/', views.logout),
]
