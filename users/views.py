import random
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView

from users.models import UserConfirmation
from users.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer, UserConfirmationSerializer


class RegisterView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(is_active=False, **serializer.data)
        confirmation = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
        return Response({'status': 'User registered', 'code': confirmation.code, 'data': serializer.data},
                        status=201)


# @api_view(['POST'])
# def register(request):
#     serializer = RegisterSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(is_active=False, **serializer.data)
#     confirmation = UserConfirmation.objects.create(user=user, code=random.randint(100000, 999999))
#     return Response({'status': 'User registered', 'code': confirmation.code, 'data': serializer.data},
#                     status=201)


class ConfirmationView(APIView):
    serializer_class = UserConfirmationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']
        confirmation = get_object_or_404(UserConfirmation, code=code)
        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()
        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)


# @api_view(['POST'])
# def confirm_code(request):
#     serializer = UserConfirmationSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     code = serializer.validated_data['code']
#     confirmation = get_object_or_404(UserConfirmation, code=code)
#     user = confirmation.user
#     user.is_active = True
#     user.save()
#     confirmation.delete()
#     token, created = Token.objects.get_or_create(user=user)
#     return Response({'status': 'User activated', 'token': token.key}, status=status.HTTP_200_OK)

class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 1 - найти пользователя в базе данных
        # user = authenticate(**serializer.data)  # None or User

        # 2 - найти пользователя в базе данных
        user = authenticate(username=serializer.validated_data['username'],
                            password=serializer.validated_data['password'])

        if user:
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            user.save()
            return Response({'token': token.key}, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# @api_view(['POST'])
# def login(request):
#     serializer = LoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#
#     # 1 - найти пользователя в базе данных
#     # user = authenticate(**serializer.data)  # None or User
#
#     # 2 - найти пользователя в базе данных
#     user = authenticate(username=serializer.validated_data['username'],
#                         password=serializer.validated_data['password'])
#
#     if user:
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})
#
#     return Response('Invalid credentials', status=400)


class ProfileView(APIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)
        return Response({'data': serializer.data}, status=200)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def profile(request):
#     user = request.user
#     serializer = ProfileSerializer(user)
#
#     return Response({'data': serializer.data}, status=200)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'message': 'User is already logged out'}, status=status.HTTP_200_OK)


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def logout(request):
#     try:
#         token = Token.objects.get(user=request.user)
#         token.delete()
#         return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)
#     except Token.DoesNotExist:
#         return Response({'message': 'User is already logged out'}, status=status.HTTP_200_OK)
