from django.contrib import admin
from .models import Category, Author, Blog, Gallery, Header

admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Header)


class GalleryAdmin(admin.StackedInline):
    model = Gallery


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    inlines = (GalleryAdmin,)
