from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_dict = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    phones = Phone.objects.all()
    sort_key = request.GET.get('sort')

    if sort_key:
        phones = phones.order_by(sort_dict.get(sort_key, 'name'))
    return render(
        request,
        'catalog.html',
        context={'phones': phones}
    )


def show_product(request, slug):
    phones_obj = Phone.objects.filter(slug=slug)
    template = 'product.html'
    for phone in phones_obj:
        data = {
            'name': phone.name,
            'release_date': phone.release_date,
            'price': phone.price,
            'image': phone.image,
            'lte_exists': phone.lte_exists
        }
    context = {'phone': data}
    return render(request, template, context)
