from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic import View
from django.http import JsonResponse
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm
from .models import Message
from django.shortcuts import redirect
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt
def cont(request):
    if request.method == 'POST':
        namm = request.POST['namm']
        emm = request.POST['emm']
        mess = request.POST['mess']
        print(namm)
        print(emm)
        print(mess)


        Message.objects.create(
        name = namm,
        email = emm,
        message = mess
        )

        return HttpResponse(status=200)

def testt(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass  # does nothing, just trigger the validation
    else:
        form = ContactForm()
    return render(request, 'email-test.html', {'form': form})

def post_new(request):
    form = ContactForm()
    return render(request, 'opening/email-test.html', {'form': form})

def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(name, message, email, ['twoodhouse97@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('thanks')
    return render(request, "opening/email-test.html", {'form': form})

def thanks(request):
    return HttpResponse('Thank you for your message.')

def contactMe(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'progInput.html', {'form': form})

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def tele(request):
    context = {

    }
    return render(request, 'opening/tele2.html', context)

def falling(request):
    context = {

    }
    return render(request, 'opening/falling.html', context)

def col_change(request):
    context = {

    }
    return render(request, 'opening/spint.html', context)

def twhome(request):
    context = {

    }
    return render(request, 'opening/loadingscreen.html', context)

def twPast(request):
    context = {

    }
    return render(request, 'pastWork.html', context)

def twabout(request):
    context = {

    }
    return render(request, 'twwdabout.html', context)

def twcontact(request):
    context = {

    }
    return render(request, 'contact.html', context)


def twwdabout(request):

    context = {

    }

    return render(request, 'twwdabout.html', context)
