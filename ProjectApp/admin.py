from django.contrib import admin
from .models import Category, Project, Gallery, Detail

admin.site.register(Category)


class GalleryAdmin(admin.StackedInline):
    model = Gallery
    extra = 2


class DetailAdmin(admin.StackedInline):
    model = Detail


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = (GalleryAdmin, DetailAdmin)
