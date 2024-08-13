from django.urls import path
from product.views import BrandApiView, CreateBrandApiView, CategoryApiView, \
    CreateCategoryApiView, ProductTypeApiView, CreateProductTypeApiView

urlpatterns = [
    path('brand/<int:pk>/', BrandApiView.as_view(), name='get-brand'),
    path('brand/create/', CreateBrandApiView.as_view(), name='create-brand'),
    path('category/<int:pk>/', CategoryApiView.as_view(), name='get-category'),
    path('category/create/', CreateCategoryApiView.as_view(), name='create-category'),
    path('productType/<int:pk>/', ProductTypeApiView.as_view(), name='get-productType'),
    path('productType/create/', CreateProductTypeApiView.as_view(), name='create-productType'),
]
