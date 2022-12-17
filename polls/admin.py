from django.contrib import admin
from .models import Question, Choice



class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text']  # 필드 순서 변경
    # fieldsets = [('Question Statement', {'fields': ['question_text']}),
    #             ('Date information', {'fields': ['pub_date']}),  # 필드를 분리해서 보여주기
    # ]

    # fieldsets = [('Question Statement', {'fields': ['question_text']}),
    #              ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),  # 필드 접기
    # ]

    # Question 및 Choice를 한 화면에서 변경하기
    # class ChoiceInline(admin.StackedInline):
    #     model = Choice
    #
    # extra = 3
    #
    # class QuestionAdmin(admin.ModelAdmin):
    #     fieldsets = [
    #         (None, {'fields': ['question_text']}),
    #         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #     ]
    #
    # inlines = [ChoiceInline]  # Choice 모델 클레스 같이 보기

    # 테이블 형식으로 보여주기
    class ChoiceInline(admin.TabularInline):
        model = Choice

    extra = 3

    class QuestionAdmin(admin.ModelAdmin):
        fieldsets = [
            (None, {'fields': ['question_text']}),
            ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        ]

    inlines = [ChoiceInline]  # Choice 모델 클레스 같이 보기
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date'] # 필터 사이드바 추가
    search_fields = ['question_text'] # 검색박스 추가 (question_text 기준으로 검색 가능)

# Register your models here.

admin.site.register(Question, QuestionAdmin) # 어드민에서 Question 관리하기
admin.site.register(Choice) # 답변 테이블 추가
