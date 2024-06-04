from django.db import models

# external models
from authentication.models.user_models import UserModified
from .product_models import Product


class Cart(models.Model):
    user_id = models.OneToOneField(
        to=UserModified,
        unique=True,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of #{self.user_id}"

    class Meta:
        db_table = "user_carts"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(models.Model):
    cart_id = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    qty = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"{self.product_id} + {self.cart_id}"

    class Meta:
        db_table = "cart_items"
        verbose_name = "cart item"
        verbose_name_plural = "cart items"
