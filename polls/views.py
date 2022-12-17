from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic # 제너릭

# Create your views here.

# 클래스형뷰(제너릭뷰)
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    """Return the last five published questions."""
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    for id_check in request.POST.getlist('choice'):
        try:
            selected_choice = question.choice_set.get(pk=id_check)  # 체크박스로 선택한 답변 id 찾아오기
        except(KeyError, Choice.DoesNotExist):  # 예외발생 - 못찾은 경우
            return render(request, 'polls/detail.html', {  # 에러메시지를 담아 render함수 전달
                'question': question,
                'error_message': "You didn't select a choice.",
            })
        else:
            selected_choice.votes += 1  # 선택한 답변의 카운트를 1 증가시킴
            selected_choice.save()  # 변경된 사항 저장

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))  # 여기 끝에 쉼표 넣어야 함

# 차트 만들기 기능
def make_chart_data(data_question) :
    my_data = list()

    for choice in data_question.choice_set.all() :
        my_dict = dict()
        my_dict['name'] = choice.choice_text
        my_dict['y'] = choice.votes
        my_data.append(my_dict)

    chart_data = [{
        'name' : 'Votes',
        'colorByPoint' : 'true',
        'data' : my_data,
    }]

    return chart_data

# 차트 결과화면 기능
import json
def result_chart(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)

    chart_data = make_chart_data(question)
    dump = json.dumps(chart_data)

    chart_title = {
        'text' : '투표결과 <br>' + question.question_text
    }

    dump_title = json.dumps(chart_title)

    return render(request, 'polls/chart.html', {'chart_data' : dump, 'chart_title' : dump_title})


# 삭제기능 추가
def Question_delete(request, question_id) :
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return redirect('polls:index')

