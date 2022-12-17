import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model) :
    question_text = models.CharField(max_length=200)  # 최대 200자까지 제한
    pub_date = models.DateTimeField('date published') # 날짜나 시간을 다루는 필드 (안에 문구는 설명)

    def __str__(self):
        return self.question_text

    def was_published_recently(self): # 등록된 질문이 하루안에 등록된 경우에만(즉 최신질문일경우만 true)
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # 지금 시간에서 질문이 등록된 시간의 차이 계산

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model) :
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 외래키 설정
    # ↑ 참조하는 테이블의 행이 삭제되면 대응되는 행들도 같이 삭제, 갱신되게 하기
    choice_text = models.CharField(max_length=200) # 최대 200자까지 제한
    votes = models.IntegerField(default=0)  # 기본값(초기값) 0 (버튼)

    def __str__(self):
        return self.choice_text
