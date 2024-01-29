from django.urls import path
from movie_app import views


urlpatterns = [
    path('directors/', views.directors_view),
    path('directors/<int:id>/', views.director_view),
    path('movies/', views.movies_view),
    path('movies/<int:id>/', views.movie_view),
    path('movies/reviews/', views.movies_reviews_view),
    path('reviews/', views.reviews_view),
    path('reviews/<int:id>/', views.review_view),
]