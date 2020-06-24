from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from core import models


# chnage for adding group start /..........
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.admin.widgets import FilteredSelectMultiple    
from django.contrib.auth.models import Group


User = get_user_model()

# Create ModelForm based on the Group model.
class GroupAdminForm(forms.ModelForm):
    class Meta:
        model = Group
        exclude = []

    # Add the users field.
    users = forms.ModelMultipleChoiceField(
         queryset=User.objects.all(), 
         required=False,
         # Use the pretty 'filter_horizontal widget'.
         widget=FilteredSelectMultiple('users', False)
    )

    def __init__(self, *args, **kwargs):
        # Do the normal form initialisation.
        super(GroupAdminForm, self).__init__(*args, **kwargs)
        # If it is an existing group (saved objects have a pk).
        if self.instance.pk:
            # Populate the users field with the current Group users.
            self.fields['users'].initial = self.instance.user_set.all()

    def save_m2m(self):
        # Add the users to the Group.
        self.instance.user_set.set(self.cleaned_data['users'])

    def save(self, *args, **kwargs):
        # Default save
        instance = super(GroupAdminForm, self).save()
        # Save many-to-many data
        self.save_m2m()
        return instance


# change for adding group model end /..........


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

class ConfigDataAdmin(admin.ModelAdmin):
    list_display =['config_name']


# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Tag)


admin.site.register(models.Ingredient, IngredientAdmin)
admin.site.register(models.Recipe, RecipeAdmin)
admin.site.register(models.Restaurant, RestaurantAdmin)
admin.site.register(models.ReviewRestaurant, ReviewRestaurantAdmin)
admin.site.register(models.Booking, BookingAdmin)
admin.site.register(models.ConfigData, ConfigDataAdmin)

