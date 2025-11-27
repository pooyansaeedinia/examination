from django.shortcuts import render
from rest_framework.generics import ListAPIView

from questions.models import Examination
from questions.serializers import QuestionSerializer


class QuestionList(ListAPIView):
    queryset = Examination.objects.all()
    serializer_class = QuestionSerializer
