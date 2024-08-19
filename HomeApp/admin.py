from django.contrib import admin
from .models import Hero, Partner, Testimonial, TestItems, AboutOne, AboutTwo, Counter

admin.site.register(Hero)
admin.site.register(Partner)
admin.site.register(AboutOne)


class ItemAdmin(admin.StackedInline):
    model = TestItems


@admin.register(Testimonial)
class TestAdmin(admin.ModelAdmin):
    inlines = (ItemAdmin,)


class CounterAdmin(admin.StackedInline):
    model = Counter


@admin.register(AboutTwo)
class AboutAdmin(admin.ModelAdmin):
    inlines = (CounterAdmin,)
