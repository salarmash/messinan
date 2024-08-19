from django.contrib import admin
from .models import Header, Service, Item

admin.site.register(Header)


class ItemAdmin(admin.StackedInline):
    model = Item
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    inlines = (ItemAdmin,)
