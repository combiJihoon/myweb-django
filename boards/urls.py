from django.urls import path, include
from . import views

app_name = 'boards'

urlpatterns = [
    path('board/', views.BoardView.as_view(), name='board-list'),
    path('board/<int:pk>/', views.BoardDetailView.as_view(), name='board-detail')
    #     path('board/<int:pk>/', views.BoardDetailView.as_view(), name='board-detail'),
    #     path('board/create/', views.BoardCreateView.as_view(), name='board-create'),
    #     path('board/<int:pk>/update/',
    #     views.BoardUpdateView.as_view(), name='board-update'),
    #     path('board/<int:pk>/delete/',
    #     views.BoardDeleteView.as_view(), name='board-delete')
]
