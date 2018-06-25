from django.contrib import admin

from .models import FeedItem, RegisteredUser


@admin.register(FeedItem)
class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ('user',)
