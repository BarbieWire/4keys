from typing import Iterable
from django.db import models

from django.utils.text import slugify
import random
import string


class Category(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey(
        to='self',
        related_name='children',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    def __str__(self):
        return "Product: ${self.name}"

    class Meta:
        db_table = "categories"
        verbose_name = "category"
        verbose_name_plural = "categories"


class Brand(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "brands"
        verbose_name = "brand"
        verbose_name_plural = "brands"


class Product(models.Model):
    category = models.ForeignKey(
        to=Category,
        null=False,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        Brand, 
        null=True,
        on_delete=models.CASCADE,
    )
    
    name = models.TextField(max_length=500, help_text="up to 500 symbols")
    description = models.TextField(help_text="unlimited text length")
    color = models.CharField(max_length=15)

    vendor_code = models.SlugField(
        unique=True,
        blank=True, 
        help_text="automatically populates with unique slug (not required)"
    )

    normal_price = models.DecimalField(max_digits=8, decimal_places=2)
    price_after_discount = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        blank=True, 
        null=True, 
        help_text="leave blank if discount not applicable"
    )

    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    # always mutable
    views = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    def generate_random_slug(self, *args, **kwargs):
        return slugify(''.join(random.choices(string.ascii_letters + string.digits, k=9)))

    def save(self, *args, **kwargs):
        if not self.vendor_code:
            # Generate a random slug
            slug = self.generate_random_slug()
            # Check if the slug is unique, if not, regenerate
            while Product.objects.filter(vendor_code=slug).exists():
                slug = self.generate_random_slug()
            self.vendor_code = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Product: {self.name}"

    class Meta:
        db_table = "products"
        verbose_name = "product"
        verbose_name_plural = "product"
        ordering = ["-date_created"]


# this section represents Entity-Attribute-Value (EAV) pattern 
# to store information regarding product attributes
class ProductAttribute(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Product attribute"
        verbose_name_plural = "Product attributes"


class ProductAttributeValue(models.Model):
    value = models.TextField()
    product = models.ForeignKey(
        to=Product,
        on_delete=models.DO_NOTHING,
        null=False,
        related_name="attributes"
    )
    attribute = models.ForeignKey(
        to=ProductAttribute,
        null=False,
        on_delete=models.DO_NOTHING,
        related_name="attribute_name"
    )

    def __str__(self) -> str:
        return f"[{self.product.name}] {self.attribute.name}: {self.value}" 

    class Meta:
        verbose_name = "Product attribute value"
        verbose_name_plural = "Product attribute values"


def upload_to(instance, filename):
    return f'products/{filename}'


class ProductPicture(models.Model):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.DO_NOTHING,
        null=False,
        related_name="pictures"
    )
    picture = models.ImageField(
        upload_to=upload_to,
        null=False
    )
    
    def __str__(self):
        return f'picture for {self.product.name}'

    class Meta:
        verbose_name_plural = "Product pictures"
        verbose_name = "Product picture"
