from rest_framework import serializers
from movie_app.models import Director, Movie, Review


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'description', 'duration')


class DirectorSerializer(serializers.ModelSerializer):
    movies_count = serializers.SerializerMethodField()

    class Meta:
        model = Director
        fields = ('id', 'name', 'movies_count')

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


class DirectorsValidateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=125)

    def create(self, validated_data):
        name = validated_data.get('name')
        director = Director.objects.create(
            name=name
        )
        return director

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class MoviesValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    directors_id = serializers.IntegerField()

    def validate_directors_id(self, value):
        try:
            Director.objects.get(id=value)
        except Director.DoesNotExist as e:
            raise serializers.ValidationError(str(e))

        return value

    def create(self, validated_data):
        title = validated_data.get('title')
        description = validated_data.get('description')
        duration = validated_data.get('duration')
        directors_id = validated_data.get('directors_id')
        # try:
        #     director = Director.objects.get(id=directors_id)
        # except Director.DoesNotExist:
        #     return Response({'error': 'Director not found'}, status=404)
        movie = Movie.objects.create(
            title=title,
            description=description,
            duration=duration,
            directors_id=directors_id
        )
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.directors_id = validated_data.get('directors_id', instance.directors_id)
        instance.save()
        return instance


class ReviewsValidateSerializer(serializers.Serializer):
    text = serializers.CharField()
    movie_id = serializers.IntegerField()
    stars = serializers.IntegerField()

    def validate_movie_id(self, value):
        try:
            Movie.objects.get(id=value)
        except Movie.DoesNotExist as e:
            raise serializers.ValidationError(str(e))

        return value

    def create(self, validated_data):
        text = validated_data.get('text')
        movie_id = validated_data.get('movie_id')
        stars = validated_data.get('stars')
        review = Review.objects.create(
            text=text,
            movie_id=movie_id,
            stars=stars)
        return review
