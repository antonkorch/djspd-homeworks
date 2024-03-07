from rest_framework import serializers
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['product', 'text', 'mark', 'created_at']

class ReviewListingField(serializers.RelatedField):
    def to_representation(self, value):
        return {'text' : value.text, 'mark' : value.mark}


class ProductListSerializer(serializers.Serializer):
    title = serializers.CharField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)


class ProductDetailsSerializer(serializers.ModelSerializer):
    #comments = ReviewSerializer(many=True, read_only=True)
    comments = ReviewListingField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'comments']
