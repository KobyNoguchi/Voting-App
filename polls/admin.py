from django.contrib import admin

from .models import Question

# admin.site.register(Question) # Uncomment if tutorial 6 edit doesnt work
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

admin.site.register(Question, QuestionAdmin)
