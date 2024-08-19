from django.contrib import admin
from .models import Category, Author, Blog, Gallery

admin.site.register(Category)
admin.site.register(Author)


class GalleryAdmin(admin.StackedInline):
    model = Gallery


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (GalleryAdmin,)
