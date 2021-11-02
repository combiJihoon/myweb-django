import json
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from .models import Board
from django.contrib.auth import get_user_model


class BoardCreateTest(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = get_user_model().objects.create_user(
            email="test@test.com", name="test", password="test123!!!"
        )
        self.client.force_authenticate(self.user)

    def test_board_post_success(self):
        board_info = {
            "title": "게시판 테스트입니다.",
            "content": "게시판 테스트입니다.",
        }
        response = self.client.post(
            "/board/",
            json.dumps(board_info),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 201)


class BoardPutTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email="test@test.com", name="test", password="test123!!!"
        )
        self.board = Board.objects.create(title="제목", content="내용", author=self.user)

    def test_board_put_unauthorized_user(self):
        board_info = {
            "title": "게시판 수정 테스트.",
            "content": "게시판 수정 테스트",
        }
        response = self.client.put(
            "/board/1/",
            json.dumps(board_info),
            content_type="application/json",
        )
        self.assertEqual(response.status_code, 401)
