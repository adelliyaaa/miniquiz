from django.urls import path


from myapp.views.index import index, create, choice, login_view, login_student, teacher, student_registration, \
    all_categories, category_questions, submit_answer, index2, results

urlpatterns = [
    path("", index, name="index"),
    path("create", create, name="create"),
    path("index2", index2, name="index2"),
    path("student_registration", student_registration, name="student_registration"),
    path("choice", choice, name="choice"),
    path('login_view/', login_view, name='login_view'),
    path('login_student/', login_student, name='login_student'),
    path('teacher', teacher, name='teacher'),
    path('all-categories/', all_categories, name='all-categories'),
    path('category-questions/<int:cat_id>/', category_questions, name='category-questions'),
    path('submit-answer/<int:cat_id>/<int:quest_id>', submit_answer, name='submit_answer'),
    path('results', results, name='results'),



]

