# base user models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# base models
from django.db import models

from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not all([password, email]):
            raise ValueError("User's email and password fields have to be filled")

        email = self.normalize_email(email)
        user = self.model(email=email)
        user.is_active = False
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        superuser = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        superuser.is_staff = True
        superuser.is_admin = True
        superuser.is_superuser = True
        superuser.is_active = True

        superuser.save()
        return superuser


class UserModified(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255)
    profile_picture = models.ImageField(null=True, upload_to="users/profile_pictures", blank=True)
    username = models.TextField(max_length=128, null=True, blank=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_join = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(auto_now=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs) -> None:
        if not self.username:
            self.username = f"user_{self.id}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    def get_tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    class Meta(AbstractBaseUser.Meta):
        verbose_name = "User"
        verbose_name_plural = "Users"
