from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from user.models import CustomUser, AccountUser
from user.serializers import CustomUserSerializer, AccountSerializer


class CreateUserApiView(ListCreateAPIView):
    serializer_class = CustomUserSerializer
    authentication_classes = ([])
    permission_classes = [AllowAny]

    def get_queryset(self):
        return CustomUser.objects.all()

    def post(self, request, *args, **kwargs):
        userData = {'username': request.data['username'],
                    'phoneNumber': request.data['phoneNumber'],
                    'password': request.data['password']
                    }
        serializer = CustomUserSerializer(data=userData)

        if serializer.is_valid():
            CustomUser.objects.create_user(username=userData['username'], password=userData['password'],
                                           phoneNumber=userData['phoneNumber'])

            # CustomUser.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserApiView(ListAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=request.user.id)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AccountApiView(ListCreateAPIView):
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return AccountUser.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        account = self.get_queryset()
        serializer = AccountSerializer(account)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):

        if AccountUser.objects.filter(user=request.user).exists():
            return Response({'detail': 'Account already exists for this user.'}, status=status.HTTP_400_BAD_REQUEST)

        accountData = {
            'user': request.user.id,
            'name': request.data.get('name', ''),
            'lastName': request.data.get('lastName', ''),
            'email': request.data.get('email', ''),
            'address': request.data.get('address', '')
        }
        serializer = AccountSerializer(data=accountData)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
