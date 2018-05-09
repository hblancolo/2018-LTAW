from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index_view, name='index'),
    # ex: /store/5/
    url(r'^specs/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'), # change product_id to pk because of the class view DetailView, which requires it.
    # ex: /search/
    url(r'^search/(?P<product_type>[A-Za-z]+)/$', views.search, name='search'),

    url(r'^search_results/$', views.search_view, name='search_view'),

    url(r'^buy/(?P<pk>[0-9]+)/$', views.BuyProductView.as_view(), name='buy'),

#   url(r'^add_to_cart/(?P<pk>[0-9]+)/$', views.add_to_cart, name='add_to_cart'),

    url(r'^cart/$', views.cart_view, name='cart'),

    url(r'^ajax/$', views.ajax_view, name='ajax'),


]