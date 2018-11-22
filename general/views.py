from django.shortcuts import render


def index(request):
    page = 'index.html'
    return render(request, page)


def index(request):
    page = 'index.html'
    return render(request, page)


def about(request):
    page = 'about.html'
    return render(request, page)


def contact(request):
    page = 'contact.html'
    return render(request, page)


def services(request):
    page = 'services.html'
    return render(request, page)


def warehouse(request):
    page = 'warehouse.html'
    return render(request, page)
