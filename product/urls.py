from django.urls import path
from product.views import BrandApiView, CreateBrandApiView, CategoryApiView, \
    CreateCategoryApiView, ProductTypeApiView, CreateProductTypeApiView, ProductAttributeApiView, \
    CreateProductAttributeApiView

urlpatterns = [
    path('brand/<int:pk>/', BrandApiView.as_view(), name='get-brand'),
    path('brand/create/', CreateBrandApiView.as_view(), name='create-brand'),
    path('category/<int:pk>/', CategoryApiView.as_view(), name='get-category'),
    path('category/create/', CreateCategoryApiView.as_view(), name='create-category'),
    path('type/<int:pk>/', ProductTypeApiView.as_view(), name='get-productType'),
    path('type/create/', CreateProductTypeApiView.as_view(), name='create-productType'),
    path('attribute/<int:pk>/', ProductAttributeApiView.as_view(), name='get-productAttribute'),
    path('attribute/create/', CreateProductAttributeApiView.as_view(), name='create-productAttribute'),

]
