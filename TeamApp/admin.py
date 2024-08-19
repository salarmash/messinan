from django.contrib import admin
from .models import Team, Item


class ItemAdmin(admin.StackedInline):
    model = Item
    extra = 1


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = (ItemAdmin,)
