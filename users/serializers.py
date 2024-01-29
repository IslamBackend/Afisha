from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import UserConfirmation


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class LoginSerializer(UserSerializer):
    pass


class RegisterSerializer(UserSerializer):
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("This username already exists")
        return username


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')


class UserConfirmationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfirmation
        fields = ['code']

