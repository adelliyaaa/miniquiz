from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from myapp.forms import ModuleForm, LoginForm, StudentLoginForm, StudentRegistrationForm

from myapp.models.quizcategory import QuizCategory
from myapp.models.quizquestion import QuizQuestion

from myapp.models.theory import Theory
from myapp.models.user import User



def index(request):
    theories = Theory.objects.order_by('id')
    return render(request, 'myapp/index.html', {'title': 'Главная страница сайта', 'theories': theories})


def index2(request):
    theories = Theory.objects.order_by('id')
    return render(request, 'myapp/index2.html', {'title': 'Главная страница сайта', 'theories': theories})



def teacher(request):
    theories = Theory.objects.order_by('id')
    return render(request, 'myapp/teacher.html', {'title': 'Главная страница сайта', 'theories': theories})

def results(request):
    users = User.objects.order_by('id')
    return render(request, 'myapp/results.html', {'title': 'результаты', "users": users})

def create(request):
    error = ''
    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:teacher')
        else:
            error = 'Форма была неверной'
    form = ModuleForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, "myapp/create.html", context)


def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.role = 'Student'
            user.save()
            # return redirect('index')
            return redirect('myapp:index2')
    else:
        form = StudentRegistrationForm()
    return render(request, 'myapp/student_registration.html', {'form': form})


def choice(request):
    return render(request, 'myapp/choice.html', {'title': 'Войти'})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('myapp:teacher')
            else:
                error_message = "Invalid username or password."
                return render(request, 'myapp/login_view.html', {'form': form, 'error_message': error_message})
        else:
            error_message = "Invalid form data."
            return render(request, 'myapp/login_view.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()

    return render(request, 'myapp/login_view.html', {'form': form})


def login_student(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            # return render(request, 'myapp/index.html')
            return redirect('myapp:index2')

    else:
        form = StudentLoginForm()

    return render(request, 'myapp/login_student.html', {'form': form})


def all_categories(request):
    catData = QuizCategory.objects.all()
    return render(request, 'myapp/all_categories.html', {'data': catData})


def category_questions(request, cat_id):
    category = QuizCategory.objects.get(id=cat_id)
    question = QuizQuestion.objects.filter(category=category).order_by('id').first()
    return render(request, 'myapp/category-questions.html', {'question': question, 'category': category})


def submit_answer(request, cat_id, quest_id):
    if request.method == 'POST':
        category = QuizCategory.objects.get(id=cat_id)
        question = QuizQuestion.objects.filter(category=category, id__gt=quest_id).exclude(id=quest_id).order_by('id').first()
        if 'skip' in request.POST:
            if question:
                return render(request, 'myapp/category-questions.html', {'question': question, 'category': category})

        if question:

            return render(request, 'myapp/category-questions.html', {'question': question, 'category': category})
        else:
            return HttpResponse('Больше вопросов нет!')

    else:
        return HttpResponse('Method not allowed!')



