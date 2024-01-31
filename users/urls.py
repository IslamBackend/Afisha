from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('confrim/', views.ConfirmationView.as_view()),
    path('login/', views.LoginAPIView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('logout/', views.LogoutAPIView.as_view()),
]
