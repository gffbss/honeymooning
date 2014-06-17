# from honeymooning.real_estate_main.models import Homess, Category
# from django.shortcuts import render_to_response, get_object_or_404
# from django.http import HttpResponseRedirect, HttpResponse
# from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.
# from honeymooning.real_estate_main.models import ContactForm


# def index(request):
#     return render_to_response('index.html', {
#         'categories': Category.objects.all(),
#         'posts': Homess.objects.all()[:5]
#     })
#
#
# def view_post(request, slug):
#     return render_to_response('view_post.html', {
#         'post': get_object_or_404(Blog, slug=slug)
#     })
#
#
# def view_category(request, slug):
#     category = get_object_or_404(Category, slug=slug)
#     return render_to_response('view_category.html', {
#         'category': category,
#         'posts': Homess.objects.filter(category=category)[:5]
#     })


def home(request):
    return render(request, "index.html")
#
#
def properties(request):
    return render(request, "properties.html")


def about(request):
    return render(request, "about.html", {'about': about})


def contact(request):
    return render(request, "contact.html")


def financing(request):
    return render(request, "financing.html")


def property(request):
    return render(request, "property.html")


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