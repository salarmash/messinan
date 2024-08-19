from django.contrib import admin
from .models import About, Gallery, Counter, Award, Item


class GalleryAdmin(admin.StackedInline):
    model = Gallery


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = (GalleryAdmin,)


admin.site.register(Counter)


class ItemAdmin(admin.StackedInline):
    model = Item


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):
    inlines = (ItemAdmin,)
