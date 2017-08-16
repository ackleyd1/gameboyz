from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile, Level

class ProfileInline(admin.StackedInline):
    """Inline for the User's :model:`gameboyz.core.Profile`"""
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    """New Admin for :model:`auth.User`"""
    inlines = (ProfileInline,)

admin.site.register(Level)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)