from django.urls import path
from goods import views


app_name = 'goods'


urlpatterns = [
    path('catalog/<slug:category_slug>/', views.catalog, name='index'),
    path('catalog/<slug:category_slug>/<int:page>/', views.catalog, name='index'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('product/<slug:product_slug>/', views.product, name='product'),
]