from rest_framework import serializers
from .models import Question, Answer
from django.contrib.auth.models import User


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id','title', 'body', 'tags')

    def create(self, validated_data):
        if self.context.get('id'):
            user = User.objects.get(id = self.context.get('id'))
            question = Question.objects.create(question_user=user, **validated_data)
            return question

    def update(self, instance, validated_data):
        if self.context.get('id'):
            question = Question.objects.get(id=instance.id)
            question.title = validated_data.get('title') if validated_data.get('title') else instance.title
            question.body = validated_data.get('body') if validated_data.get('body') else instance.body
            question.tags = validated_data.get('tags') if validated_data.get('tags') else instance.tags
            question.save()
            return question


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('id','answer')

    def create(self, validated_data):
        if self.context.get('user_id') and self.context.get('question_id'):
            user = User.objects.get(id = self.context.get('user_id'))
            question = Question.objects.get(id = self.context.get('question_id'))
            answer = Answer.objects.create(answer_user=user, question=question, **validated_data)
            return answer