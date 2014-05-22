from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html", {'about': about})


def contact(request):
    return render(request, "contact.html", {'contact': contact})


def loans(request):
    return render(request, "loans.html", {'loans': loans})


def inventory(request):
    return render(request, "inventory.html", {'inventory': inventory})