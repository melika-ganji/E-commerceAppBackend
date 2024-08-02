from django.urls import path

from user.views import CreateUserApiView, AccountApiView, UserApiView

urlpatterns = [
    path('', UserApiView.as_view(), name='get-user'),
    path('create/', CreateUserApiView.as_view(), name='create-user'),
    path('account/', AccountApiView.as_view(), name='get-account'),
    path('account/create/', AccountApiView.as_view(), name='create-account'),
]
