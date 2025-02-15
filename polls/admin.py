from django.contrib import admin

from .models import Question

# admin.site.register(Question) # Uncomment if tutorial 6 edit doesnt work
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
