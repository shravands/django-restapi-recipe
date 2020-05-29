import uuid
import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                       PermissionsMixin
from django.conf import settings


def recipe_image_file_path(instance, filename):
    """generate thge file path for new recipe image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/recipe/', filename)


class UserManager(BaseUserManager):
    """docstring for ClassName"""

    def create_user(self, email, password=None, **extra_fields):
        """ Creates and saves new user"""
        if not email:
            raise ValueError('Users must have email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """creates and saves a new superuser"""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """custom user model that supports using email instead of username"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'


class Tag(models.Model):
    """Tag to be used for a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Ingredient to be used in a recipe"""
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """Recipe object"""

# Adding of choices for which the recipe category belongs to

    CATEGORY_TYPE_CHOICES = (
        ('vegan', 'VEGAN'),
        ('vegetarian', 'VEGETERIAN'),
        ('non_veg', 'NON-VEG'),
        ('novalue', 'NOVALUE')
        )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=255)
    time_minutes = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    link = models.CharField(max_length=255, blank=True)
    ingredients = models.ManyToManyField('Ingredient')
    tags = models.ManyToManyField('Tag')
    image = models.ImageField(null=True, upload_to=recipe_image_file_path)
    recipe_category = models.CharField(max_length=20, choices=CATEGORY_TYPE_CHOICES, default='novalue')

    def __str__(self):
        return self.title


class Restaurant(models.Model):
    """Restaurant object"""

    GRADE_CATEGORY = (
        ('single_star', 'single_star'),
        ('two_star', 'two_star'),
        ('three_star', 'three_star'),
        ('five_star', 'five_star')
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=""
    )
    name = models.CharField(max_length=255)
    space_valible = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255, blank=True)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    restaurant_grade = models.CharField(max_length=20, choices=GRADE_CATEGORY, default=None)
    email_contact = models.EmailField(max_length=50, unique=True)
    recipes_avalible = models.ManyToManyField('Recipe')
    total_seating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class ReviewRestaurant(models.Model):
    """ReviewRestaurant object, the reviews will be based on the recipes avalible in restaurant"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=""
    )
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, default=1)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, default=1)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    comments = models.CharField(max_length=255, blank =True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Booking(models.Model):
    """Booking object, manage the bookings for the restaurant"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=""
    )
    restaurant = models.ForeignKey('Restaurant', on_delete=models.CASCADE, default=1)
    seats_number = models.IntegerField()
    time_start = models.DateTimeField(auto_now=False, auto_now_add=False)
    time_end = models.DateTimeField(auto_now=False, auto_now_add=False)
    comments = models.CharField(max_length=255, blank =True)

