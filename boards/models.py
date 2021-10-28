from django.db import models

# Create your models here.


class Board(models.Model):
    # 글의 제목, 내용, 작성일, 마지막 수정일
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(null=False)
    dt_created = models.DateTimeField(
        verbose_name="Date Created", auto_now_add=True, null=False)
    dt_modified = models.DateTimeField(
        verbose_name="Date Modified", auto_now=True, null=False)

    def __str__(self):
        return self.title
