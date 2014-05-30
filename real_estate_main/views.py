from django.shortcuts import render


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


# def loans(request):
#     return render(request, "loans.html", {'loans': loans})
#
#
# def inventory(request):
#     return render(request, "inventory.html", {'inventory': inventory})