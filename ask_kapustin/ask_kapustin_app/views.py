# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response


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
for i in xrange(30):
    questions.append({
        'title': 'Question #{}. How I can to do smth?'.format(i),
        'body': 'Badges are numerical indicators of how many items are associated with a link. Use the .badge class within span elements to create badges.',
        'nickname': "Никнейм_{}".format(i),
        'id': i,
    })


def getpagintator(parametr, request, nums_on_list):
    paginator = Paginator(parametr, nums_on_list)  # Show  nums_on_list contacts per page
    page = request.GET.get('page')
    try:
        questions1 = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        questions1 = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        questions1 = paginator.page(paginator.num_pages)
    return questions1


def index(request, page):
    questions1 = getpagintator(questions, request, 3)
    return render_to_response('index.html', {"questions1": questions1})
    # return render(request, 'index.html', {"questions": questions[:5]}, page)


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
    return render(request, 'hot.html', {'questions': questions[:3],})


def tag(request, htag, page):
    context = RequestContext(request, {
        'hash_tag': htag,
        "n_page": page,
    })
    questions1 = getpagintator(questions, request, 3)
    return render(request, 'tag.html', {'questions1': questions1, "context": context})


def error(request):
    return render(request, '404page.html')


def listing(request):
    return render('index.html', )
