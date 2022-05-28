from django.urls import path
from . import views

urlpatterns = [
    path(r'create_questions/', views.Question.as_view(), name='question'),
    path(r'answer_questions/<int:question_id>/', views.Answer.as_view(), name='answer'),
]