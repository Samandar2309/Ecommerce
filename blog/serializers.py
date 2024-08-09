from rest_framework import serializers
from .models import Ads, Tags, Contact, Category, SubCategory, Product_Images, Product, Order, Social_links


class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = SubCategory
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Images
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagsSerializer(many=True)
    product_image = ProductImageSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())
    class Meta:
        model = Order
        fields = '__all__'


class Social_linksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social_links
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    social_links = Social_linksSerializer(read_only=True)

    class Meta:
        model = Contact
        fields = '__all__'
