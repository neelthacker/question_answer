from django.db import models
from django.contrib.auth.models import User


QUESTION_TAGS = (
    ('science','Science'),
    ('maths','Maths'),
    ('hindi','Hindi'),
    ('english','English'),
    ('social','Social Science'),
)
# Create your models here.

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
         abstract = True

class Question(TimeStampedModel):
    question_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=200)
    body = models.TextField()
    tags = models.CharField(choices=QUESTION_TAGS, max_length=30)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['-created']


class Answer(TimeStampedModel):
    answer_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE)
    answer = models.TextField()
    is_show = models.BooleanField(default=True)


