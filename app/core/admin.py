from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'is_superuser','is_staff', 'is_active']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _("permissions"),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
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




admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)

admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Restaurant, RestaurantAdmin)

