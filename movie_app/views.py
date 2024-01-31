from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MoviesReviewsSerializer, \
    DirectorsValidateSerializer, MoviesValidateSerializer, ReviewsValidateSerializer


class DirectorsListCreateAPIView(ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ['name']
    ordering_fields = ['name']
    pagination_class = None


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        print(request.user)
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DirectorsValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer = serializer.save()
        serializer = DirectorSerializer(instance=serializer, many=False)
        return Response(serializer.data)


class DirectorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    lookup_field = 'id'

# @api_view(['GET', 'PUT', 'DELETE'])
# def director_view(request, id):
#     try:
#         director = Director.objects.get(id=id)
#     except Director.DoesNotExist:
#         return Response({'ERROR': f'Director {id} not found'})
#     if request.method == 'GET':
#         serializer = DirectorSerializer(instance=director)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = DirectorsValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         updated_director = serializer.update(instance=director, validated_data=serializer.validated_data)
#         serializer = DirectorSerializer(instance=updated_director, many=False)
#         return Response(serializer.data, status=200)
#
#     elif request.method == 'DELETE':
#         director.delete()
#         return Response(status=204)


class MoviesListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# @api_view(['GET', 'POST'])
# def movies_view(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = MoviesValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie = serializer.save()
#         serializer = MovieSerializer(instance=movie, many=False)
#         return Response(serializer.data, status=201)


class MovieDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesValidateSerializer
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_view(request, id):
#     try:
#         movie = Movie.objects.get(id=id)
#     except Movie.DoesNotExist as e:
#         return Response({'Error': str(e)})
#
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = MovieSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         movie = serializer.update(instance=movie, validated_data=request.data)
#         serializer = MovieSerializer(movie, many=False)
#         return Response(serializer.data, status=200)
#
#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=204)


class ReviewsListCreateAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsValidateSerializer

# @api_view(['GET', 'POST'])
# def reviews_view(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = ReviewsValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review = serializer.save()
#         serializer = ReviewSerializer(instance=review, many=False)
#         return Response(serializer.data)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewsValidateSerializer
    lookup_field = 'id'


# @api_view(['GET', 'PUT', 'DELETE'])
# def review_view(request, id):
#     try:
#         review = Review.objects.get(id=id)
#     except Review.DoesNotExist as e:
#         return Response({'ERROR!!!': str(e)})
#
#     if request.method == 'GET':
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = ReviewsValidateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         review.text = request.data.get('text', review.text)
#         review.movie_id = request.data.get('movie_id', review.movie_id)
#         review.stars = request.data.get('stars', review.stars)
#         review.save()
#         serializer = ReviewSerializer(instance=review, many=False)
#         return Response(serializer.data)
#
#     elif request.method == 'DELETE':
#         review.delete()
#         return Response(status=204)


class MoviesReviewsListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MoviesReviewsSerializer


# @api_view(['GET'])
# def movies_reviews_view(request):
#     movies = Movie.objects.all()
#     serializer = MoviesReviewsSerializer(movies, many=True)
#     return Response(serializer.data)
