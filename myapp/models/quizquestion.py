from django.db import models


from myapp.models.quizcategory import QuizCategory


class QuizQuestion(models.Model):
    category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
    question = models.TextField()
    opt_1 = models.CharField(max_length=200)
    opt_2 = models.CharField(max_length=200)
    opt_3 = models.CharField(max_length=200)
    opt_4 = models.CharField(max_length=200)
    level = models.CharField(max_length=100)
    time_limit = models.IntegerField()
    right_opt = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Questions"
        verbose_name = "Question"



    def __str__(self):
        return self.question



# class Question(models.Model):
#     quizcategory = models.ForeignKey(QuizCategory, related_name='quizcategory', on_delete=models.CASCADE)
#     question = models.CharField(max_length=500)
#     marks = models.IntegerField(default=5)
#
#     def __str__(self) -> str:
#         return self.question
#
#     def get_answers(self):
#         from myapp.models.answer import Answer
#         answer_objs = list(Answer.objects.filter(question=self))
#         random.shuffle(answer_objs)
#         data = []
#         for answer_obj in answer_objs:
#             data.append({
#                 'answer': answer_obj.answer,
#                 'is_correct': answer_obj.is_correct
#             })
#         return data
