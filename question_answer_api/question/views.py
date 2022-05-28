from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated

from .models import Question as SerializersQuestion, Answer as SerializersAnswer

from rest_framework.response import Response
from .serializers import QuestionSerializer, AnswerSerializer, QuestionAnswerSerializer
from rest_framework import status
# from rest_framework.decorators import api_view

# Create your views here.
class Question(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer_class = QuestionSerializer(data=request.data, context={'id':request.user.id})
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'message':'Data store succesfully'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Not able to store data'}, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, *args, **kwargs):
        if request.GET.get('tag'):
            queryset = SerializersQuestion.objects.filter(tags=request.GET.get('tag'))
        elif request.GET.get('user'):
            queryset = SerializersQuestion.objects.filter(question_user__id=request.GET.get('user'))
        else:
            queryset = SerializersQuestion.objects.all()
        serializer_class = QuestionSerializer(queryset, many=True)
        return Response({'data':serializer_class.data,}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        try:
            queryset = SerializersQuestion.objects.get(id=request.data.get('question_id'), question_user=request.user)
            serializer_class = QuestionSerializer(queryset, data=request.data, context={'id':request.user.id})
            if serializer_class.is_valid():
                serializer_class.save()
                return Response({'message':'Your data is updated Successfully!!'}, status=status.HTTP_201_CREATED)
            return Response({'message':'Not able to update your data'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'You are not a authorized person to edit this question'}, status=status.HTTP_400_BAD_REQUEST)


class Answer(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        serializer_class = AnswerSerializer(data=request.data, context={'user_id':request.user.id, 'question_id':kwargs.get('question_id')})
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'message':'Data store succesfully'}, status=status.HTTP_201_CREATED)
        return Response({'message':'Not able to store data'}, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            queryset = SerializersAnswer.objects.get(id=request.data.get('answer_id'))
            serializer_class = AnswerSerializer(queryset, data={'answer':queryset.answer}, context={'status':request.data.get('status')})
            if serializer_class.is_valid():
                serializer_class.save()
                return Response({'message':'Status updated Successfully!!'}, status=status.HTTP_201_CREATED)
            return Response({'message':'Not able to update status'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'message':'Answer not found'}, status=status.HTTP_400_BAD_REQUEST)

class GetQuestionAnswers(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        queryset = SerializersQuestion.objects.all()
        serializer_class = QuestionAnswerSerializer(queryset, many=True)
        return Response({'data':serializer_class.data,}, status=status.HTTP_201_CREATED)