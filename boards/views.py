from .models import Board
from .serializers import BoardSerializer, BoardDetailSerializer, BoardCreateSerializer, BoardUpdateSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView


class BoardListView(ListAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetailView(RetrieveAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardDetailSerializer


class BoardCreateView(CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardCreateSerializer


class BoardUpdateView(UpdateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardUpdateSerializer


class BoardDeleteView(DestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
