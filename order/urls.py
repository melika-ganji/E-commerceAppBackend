from django.urls import path

urlpatterns = [
    path('basket/<int:pk>/', name='get-basket'),
    path('basket/create/', name='create_basket'),
    path('basketList/<int:pk>/', name='get-basket-list'),
    path('basketList/create/', name='create-basket-list'),
    path('<int:pk>/', name='get-order'),
    path('create/', name='create-order'),
]
