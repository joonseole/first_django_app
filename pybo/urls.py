from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),    # URL alias , 다른 곳에서는 pybo:index 이렇게 사용
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
]