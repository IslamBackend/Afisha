from django.urls import path
from movie_app import views


urlpatterns = [
    path('directors/', views.directors_view),
    path('directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('movies/', views.MoviesListCreateAPIView.as_view()),
    path('movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('movies/reviews/', views.MoviesReviewsListAPIView.as_view()),
    path('reviews/', views.ReviewsListCreateAPIView.as_view()),
    path('reviews/<int:id>/', views.ReviewDetailAPIView.as_view()),
]