from rest_framework.decorators import api_view
from rest_framework.response import Response
from movie_app.models import Movie, Director, Review
from movie_app.serializers import MovieSerializer, DirectorSerializer, ReviewSerializer, MoviesReviewsSerializer


@api_view(['GET', 'POST'])
def directors_view(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(
            name=name
        )
        serializer = DirectorSerializer(instance=director, many=False)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response({'ERROR': f'Director {id} not found'})
    if request.method == 'GET':
        serializer = DirectorSerializer(instance=director)
        return Response(serializer.data)

    elif request.method == 'PUT':
        director.name = request.data.get('name', director.name)
        movie_id = request.data.get('movie_id', None)
        title = request.data.get('title', None)

        if movie_id is not None:
            try:
                movie = Movie.objects.get(id=movie_id)
                if title is not None:
                    movie.title = title
                    movie.save()
            except Movie.DoesNotExist:
                return Response({'ERROR': f'Movie {movie_id} not found'})

        director.save()

        serializer = DirectorSerializer(instance=director, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        director.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def movies_view(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        directors_id = request.data.get('directors_id')
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
        serializer = MovieSerializer(instance=movie, many=False)
        return Response(serializer.data, status=201)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    elif request.method == 'PUT':
        movie.title = request.data.get('title', movie.title)
        movie.description = request.data.get('description', movie.description)
        movie.duration = request.data.get('duration', movie.duration)
        movie.directors_id = request.data.get('directors_id', movie.directors_id)
        movie.save()
        serializer = MovieSerializer(movie, many=False)
        return Response(serializer.data, status=200)

    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def reviews_view(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        stars = request.data.get('stars')
        review = Review.objects.create(
            text=text,
            movie_id=movie_id,
            stars=stars)
        serializer = ReviewSerializer(instance=review, many=False)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist as e:
        return Response({'ERROR!!!': str(e)})

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'PUT':
        review.text = request.data.get('text', review.text)
        review.movie_id = request.data.get('movie_id', review.movie_id)
        review.stars = request.data.get('stars', review.stars)
        review.save()
        serializer = ReviewSerializer(instance=review, many=False)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=204)


@api_view(['GET'])
def movies_reviews_view(request):
    movies = Movie.objects.all()
    serializer = MoviesReviewsSerializer(movies, many=True)
    return Response(serializer.data)
