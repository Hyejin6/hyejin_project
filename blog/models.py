from django.db import models # 디폴트 기본값 지우면 안됨
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Post(models.Model) :
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # 작성자 (앱에 등록된 사용자만 가능)
    title = models.CharField(max_length=200) # 제목
    text = models.TextField() # 내용
    created_date = models.DateTimeField(default=timezone.now) # 글 작성일
    published_date = models.DateTimeField(blank=True, null=True) # 글 게시일

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

