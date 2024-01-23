from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

    def get_movies_count(self, directors):
        return directors.movies.count()


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id', 'text', 'stars')


class MoviesReviewsSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration', 'rating', 'reviews')

    def get_rating(self, obj):
        stars_sum = sum(review.stars for review in obj.reviews.all())
        reviews_count = obj.reviews.count()
        return stars_sum / reviews_count
