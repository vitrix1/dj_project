from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    context = {}
    for phone in phones:
        context[phone.id] = {
            'name': phone.name,
            'image': phone.image,
            'price': phone.price,
            'release_date': phone.release_date,
            'lte_exists': phone.lte_exists,
            'slug': phone.slug}
    print(context)
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {}
    return render(request, template, context)
