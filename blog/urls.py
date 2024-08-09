from django.urls import path
from .views import Products, ProductDetail, CategoryList, TagsList, ProductImages, Social_link, Contact, OrderList, \
    OrderDetail

app_name = 'blog'

urlpatterns = [
    path('product/', Products.as_view(), name="product"),
    path('product/<int:pk>/', ProductDetail.as_view(), name="product_detail"),
    path('category/', CategoryList.as_view(), name="category"),
    path('tags/', TagsList.as_view(), name="tags"),
    path('product/images/', ProductImages.as_view(), name="product_image"),
    path('social_link/', Social_link.as_view(), name="social_link"),
    path('contact/', Contact.as_view(), name="contact"),
    path('order/', OrderList.as_view(), name="order"),
    path('order/<int:pk>/', OrderDetail.as_view(), name="order_detail"),
]
