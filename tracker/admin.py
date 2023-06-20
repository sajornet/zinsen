from django.contrib import admin
from .models import Category, Provider, Offering

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Offering)
class OfferingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'provider', 'minimum', 'maximum')
    list_filter = ('category', 'provider')
    search_fields = ('name', 'description')