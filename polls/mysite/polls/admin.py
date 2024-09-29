from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Text", {"fields" : ["question_text"]}),
        ("Date information", {"fields":["pub_data"]}),
    ]
    
    #list_display = ["question_text","pub_data","was_published_recently"]
    #list_filter = ["pub_data"]
    #search_fields = ["question_text"]
    
    inlines = [ChoiceInline]
    #fields = ["pub_data","question_text"]
admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)
