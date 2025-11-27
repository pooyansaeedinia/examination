from django.db import models

# Create your models here.

class QuestionOptions(models.Model):
    option = models.TextField()

    def __str__(self):
        return self.option


class Examination(models.Model):
    question = models.TextField()
    option = models.ManyToManyField(QuestionOptions)
    correctOption = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f"question {self.id}"