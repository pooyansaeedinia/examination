from rest_framework import serializers
from questions.models import Examination, QuestionOptions


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOptions
        fields = ("option",)


class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    class Meta:
        model = Examination
        fields = ("question", "options", "correctOption", "points")

    @staticmethod
    def get_options(obj):
        return [opt.option for opt in obj.option.all()]