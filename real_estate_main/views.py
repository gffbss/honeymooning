from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render


# Create your views here.
# from honeymooning.real_estate_main.models import ContactForm


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


def testpage(request):
    return render(request, "testpage.html")


# class ContactView(CreateView):
#     model = ContactForm
#     form_class = ContactForm
#     template_name = "contact/contact.html"
#     success_url = "/contact/success/"
#
#     def form_valid(self, form):
#         super(ContactView,self).form_valid(form)
#         send_mail("Foo", "bar", 'from@example.com', [form.cleaned_data['email']])
#         return HttpResponseRedirect(self.get_success_url())
#
#
# class QuoteSuccessView(TemplateView):
#     template_name = "contact/contact-complete.html"

# def loans(request):
#     return render(request, "loans.html", {'loans': loans})
#
#
# def inventory(request):
#     return render(request, "inventory.html", {'inventory': inventory})