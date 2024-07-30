from rest_framework.generics import ListCreateAPIView
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from user.models import CustomUser, AccountUser
from user.serializers import CreateUserSerializer, CreateAccountSerializer


class CreateUserApiView(ListCreateAPIView):
    serializer_class = CreateUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CustomUser.objects.all()

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, user=request.user)
        serializer = CreateUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        userData = {'username': request.data['username'],
                    'phone_number': request.data['phoneNumber'],
                    'password': request.data['password']
                    }
        serializer = CreateUserSerializer(data=userData)

        if serializer.is_valid():
            CustomUser.objects.create_user(username=userData['username'], password=userData['password'],
                                           phone_number=userData['phone_number'])

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateAccountApiView(ListCreateAPIView):
    serializer_class = CreateAccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AccountUser.objects.all()

    def get(self, request, *args, **kwargs):
        account = get_object_or_404(AccountUser, user=request.user)
        serializer = CreateUserSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        accountData = {'user': request.user,
                       'name': request.data['name'],
                       'lastName': request.data['lastName'],
                       'email': request.data['email'],
                       'address': request.data['address']
                       }
        serializer = CreateAccountSerializer(data=accountData)

        if serializer.is_valid():
            AccountUser.objects.create(user=request.user, name=accountData['name'],
                                       lastName=accountData['lastName'], email=accountData['email'],
                                       address=accountData['address'])

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
