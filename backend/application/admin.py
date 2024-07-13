# admin stuff
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.html import format_html


# models
from .models import *


class ProductAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class BrandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)


class ProductAttributeValueAdmin(admin.ModelAdmin):
    pass


class ProductAttributeAdmin(admin.ModelAdmin):
    pass


class ProductPictureAdmin(admin.ModelAdmin):
    @staticmethod
    def img_tag(obj):
        return mark_safe(f"<img src={obj.picture.url} height=75px/>")

    list_display = ['img_tag']
    search_fields = (
        'product__pk', 
        'product__name', 
        'product__category__name'
    )


admin.site.register(ProductPicture, ProductPictureAdmin)
admin.site.register(ProductAttributeValue, ProductAttributeValueAdmin)
admin.site.register(ProductAttribute, ProductAttributeAdmin)


class UserCartAdmin(admin.ModelAdmin):
    fields = ("user", "created_date", "session_token")
    search_fields = ("user__username", "user__email")
    readonly_fields = ("created_date", )


class UserWishlistAdmin(admin.ModelAdmin):
    fields = (
        "user_id",
        "created_date"
    )
    search_fields = (
        "user_id__username",
        "user_id__email"
    )
    readonly_fields = ("created_date",)


class UserCartItemAdmin(admin.ModelAdmin):
    fields = ("cart", "product", "qty")


class UserWishlistItemAdmin(admin.ModelAdmin):
    fields = ("wishlist", "product", "in_cart")


admin.site.register(Cart, UserCartAdmin)
admin.site.register(Wishlist, UserWishlistAdmin)
admin.site.register(CartItem, UserCartItemAdmin)
admin.site.register(WishlistItem, UserWishlistItemAdmin)


class BannerAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.banner.url))

    image_tag.short_description = 'Image'
    list_display = ['image_tag']

admin.site.register(Banner, BannerAdmin)