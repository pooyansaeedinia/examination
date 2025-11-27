from django.contrib import admin

from questions.models import QuestionOptions, Examination

# Register your models here.

admin.site.register(QuestionOptions)
admin.site.register(Examination)