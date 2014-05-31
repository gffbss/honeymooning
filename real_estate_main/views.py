from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from contacts.models import ContactForm
from django.template import RequestContext, Context
from django import newforms as forms
from django.newforms.widgets import *
from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def home(request):
    return render(request, "index.html")


def properties(request):
    return render(request, "properties.html")


def about(request):
    return render(request, "about.html", {'about': about})


def contact(request):
    return render(request, "contact.html")


def financing(request):
    return render(request, "financing.html")


def contactview(request):
    subject = request.POST.get('topic', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')

    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['change@this.com'])
            except BadHeaderError:
            return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thankyou/')
        else:
            return render_to_response('contacts.html', {'form': ContactForm()})

        return render_to_response('contacts.html', {'form': ContactForm()},
                                  RequestContext(request))


def thankyou(request):
    return render_to_response('thankyou.html')


# def loans(request):
#     return render(request, "loans.html", {'loans': loans})
#
#
# def inventory(request):
#     return render(request, "inventory.html", {'inventory': inventory})