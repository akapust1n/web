# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def get_post_params(request):
    result = ['<p>Aplication_django</p>']
    result.append('Post:')
    result.append('<form method="post">')
    result.append('<input type="text" name = "test">')
    result.append('<input type="submit" value="Send">')
    result.append('</form>')

    if request.method == 'POST':
        result.append(request.POST.urlencode())

    if request.method == 'GET':
        if request.GET.urlencode() != '':
            result.append('Get data:')
            for key, value in request.GET.items():
                keyvalue = key + " = " + value
                result.append(keyvalue)

    return HttpResponse('<br>'.join(result))


def base(request):
    return render(request, "base.html")


questions = []
for i in xrange(3):
    questions.append({
        'title': 'Question #{}. How I can to do smth?'.format(i),
        'body': 'Badges are numerical indicators of how many items are associated with a link. Use the .badge class within span elements to create badges.',
        'nickname': "Никнейм_{}".format(i),
        'id': i,
    })


def index(request, page):
    return render(request, 'index.html', {'questions': questions,}, page)


def ask(request):
    return render(request, 'ask.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def question(request, question_id):
    context = RequestContext(request, {
        'que_id': question_id,
    })
    return render(request, 'question.html', {'questions': questions, "context": context})


def hot(request):
    return render(request, 'hot.html', {'questions': questions,})


def tag(request, htag, page):
    context = RequestContext(request, {
        'hash_tag': htag,
        "n_page": page,
    })
    return render(request, 'tag.html', {'questions': questions, "context": context})


def error(request):
    return render(request, '404page.html')
