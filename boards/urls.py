from django.urls import path, include
from . import views

app_name = 'boards'

urlpatterns = [
    path('board/', views.BoardView.as_view(), name='board-list'),
    path('board/<int:pk>/', views.BoardDetailView.as_view(), name='board-detail')
]
