from django.urls import path
from product.views import BrandApiView, CreateBrandApiView, CategoryApiView, \
    CreateCategoryApiView, ProductTypeApiView, CreateProductTypeApiView, ProductAttributeApiView, \
    CreateProductAttributeApiView, ProductApiView, CreateProductApiView, ProductAttributeValueApiView, \
    CreateProductAttributeValueApiView

urlpatterns = [
    path('brand/<int:pk>/', BrandApiView.as_view(), name='get-brand'),
    path('brand/create/', CreateBrandApiView.as_view(), name='create-brand'),
    path('category/<int:pk>/', CategoryApiView.as_view(), name='get-category'),
    path('category/create/', CreateCategoryApiView.as_view(), name='create-category'),
    path('type/<int:pk>/', ProductTypeApiView.as_view(), name='get-product-type'),
    path('type/create/', CreateProductTypeApiView.as_view(), name='create-product-type'),
    path('attribute/<int:pk>/', ProductAttributeApiView.as_view(), name='get-product-attribute'),
    path('attribute/create/', CreateProductAttributeApiView.as_view(), name='create-product-attribute'),
    path('<int:pk>/', ProductApiView.as_view(), name='get-product'),
    path('create/', CreateProductApiView.as_view(), name='create-product'),
    path('attribute/value/<int:pk>/', ProductAttributeValueApiView.as_view(), name='get-product-attribute-value'),
    path('attribute/value/create/', CreateProductAttributeValueApiView.as_view(),
         name='create-product-attribute-value'),

]
