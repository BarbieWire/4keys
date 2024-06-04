from django.db import models

# external models
from authentication.models.user_models import UserModified
from .product_models import Product


class Wishlist(models.Model):
    user_id = models.OneToOneField(
        to=UserModified,
        unique=True,
        on_delete=models.CASCADE,
        blank=True,
    )
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Wishlist of #{self.user_id}"

    class Meta:
        db_table = "user_wishlists"
        verbose_name = "wishlist"
        verbose_name_plural = "wishlists"


class WishlistItem(models.Model):
    wishlist_id = models.ForeignKey(
        to=Wishlist,
        on_delete=models.CASCADE,
        blank=True,
    )
    product_id = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    in_cart = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.wishlist_id} + {self.product_id}"

    class Meta:
        db_table = "wishlist_items"
        verbose_name = "wishlist item"
        verbose_name_plural = "wishlist items"
