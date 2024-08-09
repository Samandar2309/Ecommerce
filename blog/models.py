from django.db import models


# Create your models here.
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Ads(TimeStampedModel):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=212)
    description = models.TextField()


class Tags(TimeStampedModel):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Category(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name


class SubCategory(TimeStampedModel):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product_Images(TimeStampedModel):
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.image.name


class Product(TimeStampedModel):
    name = models.CharField(max_length=212)
    price = models.DecimalField(max_digits=500, decimal_places=2)
    description = models.TextField()
    tags = models.ManyToManyField(Tags)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_images = models.ManyToManyField(Product_Images)

    def __str__(self):
        return self.name


class Order(TimeStampedModel):
    name = models.CharField(max_length=212)
    phone = models.CharField(max_length=212)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Social_links(TimeStampedModel):
    name = models.CharField(max_length=212)
    link = models.URLField()

    def __str__(self):
        return self.name


class Contact(TimeStampedModel):
    name = models.CharField(max_length=212)
    email = models.EmailField()
    phone = models.CharField(max_length=212)
    link = models.ForeignKey(Social_links, on_delete=models.CASCADE)
    address = models.CharField(max_length=212)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
