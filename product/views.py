from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product.models import Brand, Category, ProductType, ProductAttribute
from product.serializers import BrandSerializer, CategorySerializer, ProductTypeSerializer, ProductAttributeSerializer


class BrandApiView(ListAPIView):
    serializer_class = BrandSerializer
    authentication_classes = ([])
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Brand.objects.all()

    def get(self, request, *args, **kwargs):
        brand = get_object_or_404(Brand, pk=kwargs['pk'])
        serializer = BrandSerializer(brand)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateBrandApiView(ListCreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Brand.objects.all()

    def post(self, request, *args, **kwargs):
        data = {'name': request.data.get('name')}

        parentName = request.data.get('parent')
        if parentName:
            data['parentName'] = parentName

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryApiView(ListAPIView):
    serializer_class = CategorySerializer
    authentication_classes = ([])
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Category.objects.all()

    def get(self, request, *args, **kwargs):
        category = get_object_or_404(Category, pk=kwargs['pk'])
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateCategoryApiView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Category.objects.all()

    def post(self, request, *args, **kwargs):
        data = {'name': request.data.get('name')}

        parentName = request.data.get('parent')
        if parentName:
            data['parentName'] = parentName

        serializer = self.get_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductTypeApiView(ListAPIView):
    serializer_class = ProductTypeSerializer
    permission_classes = [AllowAny]
    authentication_classes = ([])

    def get_queryset(self):
        return ProductType.objects.all()

    def get(self, request, *args, **kwargs):
        productType = get_object_or_404(ProductType, pk=kwargs['pk'])
        serializer = ProductTypeSerializer(data=productType)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProductTypeApiView(ListCreateAPIView):
    serializer_class = ProductTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProductType.objects.all()

    def post(self, request, *args, **kwargs):
        data = {'name': request.data.get('name')}

        serializer = ProductTypeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProductAttributeApiView(ListAPIView):
    serializer_class = ProductAttributeSerializer
    authentication_classes = ([])
    permission_classes = [AllowAny]

    def get_queryset(self):
        return ProductAttribute.objects.all()

    def get(self, request, *args, **kwargs):
        attribute = get_object_or_404(ProductAttribute, pk=kwargs['pk'])
        serializer = ProductAttributeSerializer(attribute)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProductAttributeApiView(ListCreateAPIView):
    serializer_class = ProductAttributeSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = ProductAttribute.objects.all()

    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'productTypeName': request.data.get('productType')
        }

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


