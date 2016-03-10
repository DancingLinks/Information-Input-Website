from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from collect_app.models import Information


def check_email(email):
    return True


def home(request):
    return HttpResponseRedirect('/index')


def index(request):
    t = get_template('index.html')
    html = t.render()
    return HttpResponse(html)


@csrf_exempt
def register(request):
    name = str(request.POST['name'])
    num = str(request.POST['num'])
    email = str(request.POST['email'])

    # if(not check_email(email)):
    #     return JsonResponse({"result": False})

    information = Information.objects.filter(num=num)

    if(len(information)<1):
        information = Information(name=name, num=num, email=email)
        information.save()
    else:
        information[0].name = name
        information[0].email = email
        information[0].save()

    return JsonResponse({"result": True})
