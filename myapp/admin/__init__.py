from django.contrib import admin


from myapp.models.theory import Theory
from myapp.models.teacher import Teacher
from myapp.models.quizquestion import QuizQuestion
from myapp.models.quizcategory import QuizCategory
from myapp.models.user import User


class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'level']



admin.site.register(User)
admin.site.register(Theory)
admin.site.register(Teacher)
admin.site.register(QuizQuestion, QuizQuestionAdmin)
admin.site.register(QuizCategory)

class UserSubmittedAnswerAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'user', 'right_answer']


