from django.urls import path
from movie_app import views


urlpatterns = [
    path('api/v1/directors/', views.directors_view),
    path('api/v1/directors/<int:id>/', views.director_view),
    path('api/v1/movies/', views.movies_view),
    path('api/v1/movies/<int:id>/', views.movie_view),
    path('api/v1/reviews/', views.reviews_view),
    path('api/v1/reviews/<int:id>/', views.review_view),
]