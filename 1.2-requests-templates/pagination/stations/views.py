from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
    data = list(csv.DictReader(csvfile))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    paginator = Paginator(data, 1)
    page = paginator.get_page(1)
    context = {
        'bus_stations': paginator,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
