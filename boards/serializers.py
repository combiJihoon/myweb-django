from .models import Board
from rest_framework import serializers


class BoardSerializer(serializers.ModelSerializer):
    board = serializers.StringRelatedField()

    class Meta:
        model = Board
        fields = ["id", "board", "title", "content", "dt_created", "dt_modified"]


class BoardDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ["id", "author", "title", "content", "dt_created", "dt_modified"]
