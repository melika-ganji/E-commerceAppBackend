from django.urls import path

from user.views import CreateUserApiView, CreateAccountApiView

urlpatterns = [
    path('create/', CreateUserApiView.as_view(), name='create-user'),
    path('create/account/', CreateAccountApiView.as_view(),name='create-account'),
]
