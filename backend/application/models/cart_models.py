from django.db import models

# external models
from authentication.models.user_models import UserModified
from .product_models import Product


class Cart(models.Model):
    user = models.OneToOneField(
        to=UserModified,
        unique=True,
        on_delete=models.CASCADE,
        null=True,
    )
    created_date = models.DateTimeField(auto_now=True)
    # if user doesn't have an account the annonymous cart will be assigned based on session id
    session_token = models.CharField(
        max_length=255, 
        unique=True, 
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Cart of {self.user if self.user_id else self.session_token}"

    class Meta:
        db_table = "user_carts"
        verbose_name = "Cart"
        verbose_name_plural = "Carts"


class CartItem(models.Model):
    cart = models.ForeignKey(to=Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    qty = models.SmallIntegerField(default=1)

    def __str__(self):
        return f"<{self.cart}> -- <{self.product}>"

    class Meta:
        db_table = "cart_items"
        verbose_name = "cart item"
        verbose_name_plural = "cart items"
