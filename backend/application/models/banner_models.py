from django.db import models


def upload_to(instance, filename):
    return f'banners/{filename}'

class Banner(models.Model):
    banner = models.ImageField(upload_to=upload_to, null=False, blank=False)
    link = models.URLField(
        blank=True, 
        null=True, 
        max_length=200, 
        help_text="some useful link which characterize banner's content"
    )

    def __str__(self) -> str:
        return f"banner_{self.pk}"

    class Meta:
        db_table = "banner"
        verbose_name = "Banner"
        verbose_name_plural = "Banners"
