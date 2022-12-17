from django.urls import path
from . import views

app_name = 'polls' # 네임스페이스 설정

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('<int:question_id>/chart/', views.result_chart, name='chart'),
    path('<int:question_id>/delete/', views.Question_delete, name='delete'),

]