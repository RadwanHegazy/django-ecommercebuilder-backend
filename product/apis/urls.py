from django.urls import path
from .views import get, create

urlpatterns = [
    path('get/<str:shop_name>/', get.GetProductList.as_view(),name='get_all_pds'),
    path('create/', create.CreateProducts.as_view(),name='create_pd'),
]