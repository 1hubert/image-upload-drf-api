"""
Database models.
"""
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.core.validators import MinValueValidator
from django.db import models


class UserManager(BaseUserManager):
    """User manager."""

    def create_user(self, username, password, **kwargs):
        """Create, save and return a new user."""
        user = self.model(username=username, **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Create, save and return a new superuser (admin)."""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class ThumbnailSize(models.Model):
    """Thumbnail size model for account tiers."""
    height = models.IntegerField(
        validators=[MinValueValidator(1)]
    )


class AccountTier(models.Model):
    """Account Tier model for members."""
    plan_name = models.CharField(unique=True, max_length=60)
    preserve_original_image = models.BooleanField(default=False)
    allow_expiring_links = models.BooleanField(default=False)
    allowed_thumbnail_sizes = models.ManyToManyField(ThumbnailSize, related_name='account_tiers')


class User(AbstractBaseUser, PermissionsMixin):
    """User model for members and admins."""
    username = models.CharField(unique=True, max_length=60)
    is_staff = models.BooleanField(default=False)
    tier = models.ForeignKey(
        AccountTier,
        on_delete=models.CASCADE,
        related_name='users',
        null=True
    )
    objects = UserManager()

    USERNAME_FIELD = 'username'
