from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'is_superuser','is_staff', 'is_active', 'is_customer']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _("permissions"),
            {'fields': ('is_active', 'is_staff', 'is_superuser', 'is_customer')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

# chnage  of the view in the admin page
class RecipeAdmin(admin.ModelAdmin):
    list_display =['title', 'user', 'time_minutes', 'price', 'recipe_category']
    list_filter =['recipe_category']


class IngredientAdmin(admin.ModelAdmin):
    list_display =['name', 'user']
    list_filter =['user']

class RestaurantAdmin(admin.ModelAdmin):
    list_display =['name', 'user', 'location', 'rating', 'restaurant_grade']
    list_filter =['restaurant_grade']


class ReviewRestaurantAdmin(admin.ModelAdmin):
    list_display =['id', 'restaurant', 'recipe', 'user', 'rating', 'created_at']
    list_filter =['restaurant', 'user']


class BookingAdmin(admin.ModelAdmin):
    list_display =['id', 'restaurant', 'user', 'seats_number', 'is_active']
    list_filter =['restaurant', 'user', 'is_active']




admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)
admin.site.register(models.ConfigData)

admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Restaurant, RestaurantAdmin)
admin.site.register(models.ReviewRestaurant, ReviewRestaurantAdmin)
admin.site.register(models.Booking, BookingAdmin)

