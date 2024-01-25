from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration')


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()
    movies = MovieSerializer(many=True)

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count', 'movies')

    def get_movies_count(self, directors):
        return directors.movies.count()


class ReviewSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'movie_title', 'stars', 'text')

    def get_movie_title(self, review):
        if review.movie:
            return review.movie.title
        return None


class MoviesReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'rating', 'reviews')

    def get_rating(self, obj):
        stars_sum = sum(review.stars for review in obj.reviews.all())
        reviews_count = obj.reviews.count()
        return stars_sum / reviews_count if reviews_count > 0 else 0
