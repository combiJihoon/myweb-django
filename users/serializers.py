from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

User = get_user_model()


# 회원가입
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name", "password"]
        extra_kwagrs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user


# 로그인
class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to login with provided credentials.")


# 접속 유지 확인
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "name"]
