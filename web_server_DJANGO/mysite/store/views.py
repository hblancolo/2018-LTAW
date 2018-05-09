from django.http import Http404
from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import generic
from django.core.context_processors import csrf
from django.http import HttpResponse
import datetime

from .models import Product, BuyOrder

import re


def index_view(request):

    latest_product_list = Product.objects.order_by('-pub_date')

    response = render(request, 'store/index.html', {'latest_product_list': latest_product_list})

    if 'cart' in request.COOKIES:  # if i have already set the cookie 'cart'
        print('The cookie "cart" already exists')
    else:  # if it is the first product, we create the cookie cart with the product
        response.set_cookie('cart', None, expires=expire_date(1))  # expire_date is a function

    return response


class DetailView(generic.DetailView):
    model = Product
    template_name = 'store/detail.html'


class BuyProductView(generic.TemplateView):
    template_name = 'store/buy-product-form.html'

    def get(self, request, pk):
        product = Product.objects.filter(pk=pk)[0]
        return render(request, self.template_name, {'product': product})

    def post(self, request, pk):
        theOrder = BuyOrder()
        theOrder.product_name = request.POST.get("product_name", "")
        theOrder.user_name = request.POST.get("user_name", "")
        theOrder.shipping_address = request.POST.get("shipping_address", "")
        theOrder.zip_code = request.POST.get("zip_code", "")
        theOrder.save()

        return render(request, 'store/order_confirmation.html')


def search(request, product_type):  # this one for the 'bikes' 'books' and 'cd' tabs
    product_list = Product.objects.filter(product_type=product_type)
    if (len(product_list) == 0):
        raise Http404("Product does not exist")

    context = {
        'latest_product_list': product_list,
    }
    return render(request, 'store/index.html', context)


def normalize_query(query_string,
                    findterms=re.compile(r'"([^"]+)"|(\S+)').findall,
                    normspace=re.compile(r'\s{2,}').sub):
    ''' Splits the query string in individual keywords, getting rid of unnecessary spaces
        and grouping quoted words together.
        Example:

        >>> normalize_query('  some random  words "with   quotes  " and   spaces')
        ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    '''
    return [normspace(' ', (t[0] or t[1]).strip()) for t in findterms(query_string)]


def get_query(query_string, search_fields):
    ''' Returns a query, that is a combination of Q objects. That combination
        aims to search keywords within a model by testing the given search fields.

    '''
    query = None # Query to search for every search term
    terms = normalize_query(query_string)
    for term in terms:
        or_query = None # Query to search for a given term in each field
        for field_name in search_fields:
            q = Q(**{"%s__icontains" % field_name: term})
            if or_query is None:
                or_query = q
            else:
                or_query = or_query | q
        if query is None:
            query = or_query
        else:
            query = query & or_query
    return query


def search_view(request):  # this function is used for the search bar
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']

        entry_query = get_query(query_string, ['product_type', 'product_name'])

        found_entries = list(Product.objects.filter(entry_query))
    return render(request, 'store/index.html', {'query_string': query_string, 'latest_product_list': found_entries})


'''def add_to_cart(request, pk):
    latest_product_list = Product.objects.order_by('-pub_date')
    product = Product.objects.filter(pk=pk)[0]

    product_name_for_cookie = '-'.join(product.product_name.split(" "))  # takes the name of the product and joins it
                                                                 # with - to make it usable in the cookies

    response = render(request, 'store/index.html', {'latest_product_list': latest_product_list})

    if 'cart' in request.COOKIES:  # if there are already products in the cart
        current_cart_products = request.COOKIES['cart']
        current_cart_products += '/' + product_name_for_cookie
        response.set_cookie('cart', current_cart_products, expires=expire_date(1))
    else:  # if it is the first product, we create the cookie cart with the product
        response.set_cookie('cart', product_name_for_cookie, expires=expire_date(1))

    return response
'''

def cart_view(request):
    total_cost = 0
    cart = []

    for cookie_name in request.COOKIES:
        if cookie_name == 'cart':
            products_in_cart = request.COOKIES['cart'].split(',')[0:-1]  # range applied only for not to take the last element which is an empty string
            for product_id in products_in_cart:
                product = Product.objects.get(pk=product_id)
                cart.append(product)

            for product in cart:
                total_cost += product.product_price

    return render(request, 'store/cart.html', {'cart': cart, 'total_cost': total_cost})


def expire_date(days_expire):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60

    return datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")


def ajax_view(request):
    related_names = "["
    search_text = request.body.decode("utf-8")
    related_products = Product.objects.all().filter(product_name__icontains=str(search_text))
    for product in related_products:
        related_names += '"' + product.product_name + '",'

    related_names = related_names[0:-1]
    related_names += "]"

    return HttpResponse(related_names)








