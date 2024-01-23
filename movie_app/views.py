from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MoviesReviewsSerializer


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response({'ERROR': f'Director {id} not found'})

    serializer = DirectorSerializer(instance=director)
    return Response(serializer.data)


@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist as e:
        return Response({'Error': str(e)})
    serializer = MovieSerializer(movie)
    return Response(serializer.data) @ api_view(['GET'])


def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist as e:
        return Response({'Error': str(e)})
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist as e:
        return Response({'ERROR!!!': str(e)})
    serializer = ReviewSerializer(review)
    return Response(serializer.data)


@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MoviesReviewsSerializer(movies, many=True)
    return Response(serializer.data)