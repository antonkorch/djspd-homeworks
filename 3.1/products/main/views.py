from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer

from .models import Product, Review

@api_view(['GET'])
def products_list_view(request):
    products = Product.objects.all()
    result = ProductListSerializer(products, many=True)
    return Response(result.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(status=404)
            
        result = ProductDetailsSerializer(product)
        return Response(result.data)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        try:
            reviews = Review.objects.filter(product=product_id)
        except Review.DoesNotExist:
            return Response(status=404)

        params = request.query_params
        if 'mark' in params:
            reviews = reviews.filter(mark=params['mark'])
        result = ReviewSerializer(reviews, many=True)
        return Response(result.data)
