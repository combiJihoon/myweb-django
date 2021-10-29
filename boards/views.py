from .models import Board
from .serializers import BoardSerializer, BoardDetailSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class BoardView(APIView):
    def get(self, request):
        board_list = Board.objects.all()
        board_list_serializer = BoardSerializer(
            board_list, many=True)
        return Response(board_list_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        board_serializer = BoardSerializer(data=request.data)

        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BoardDetailView(APIView):
    def get_object(self, pk):
        try:
            return Board.objects.get(pk=pk)
        except Board.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        board_detail = self.get_object(pk)
        board_detail_serializer = BoardDetailSerializer(board_detail)
        return Response(board_detail_serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        board_detail = self.get_object(pk)
        board_serializer = BoardSerializer()(
            board_detail, data=request.data)

        if board_serializer.is_valid():
            board_serializer.save()
            return Response(board_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(board_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        board_detail = self.get_object(pk)
        board_detail.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
