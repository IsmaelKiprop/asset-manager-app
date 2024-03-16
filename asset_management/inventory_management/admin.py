from django.contrib import admin
from .models import IntangibleAsset, IntangibleAssetCategory, IntangibleAssetIndustry, AssetDocument, ConcernedPeople, ExpiringAsset, TotalAssetValue

@admin.register(IntangibleAssetIndustry)
class IntangibleAssetIndustryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(IntangibleAssetCategory)
class IntangibleAssetCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'industry']

@admin.register(IntangibleAsset)
class IntangibleAssetAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'date_registered', 'expiring_date', 'value', 'owner', 'date_created', 'date_modified']
    list_filter = ['category', 'owner', 'date_created', 'date_modified']
    search_fields = ['name', 'owner__username']
    date_hierarchy = 'date_created'

@admin.register(AssetDocument)
class AssetDocumentAdmin(admin.ModelAdmin):
    list_display = ['asset', 'description']
    search_fields = ['asset__name']

@admin.register(ConcernedPeople)
class ConcernedPeopleAdmin(admin.ModelAdmin):
    list_display = ['asset', 'name', 'title', 'contact_details']
    search_fields = ['asset__name']

@admin.register(ExpiringAsset)
class ExpiringAssetAdmin(admin.ModelAdmin):
    list_display = ['asset', 'notification_date', 'notified']
    list_filter = ['notification_date', 'notified']
    search_fields = ['asset__name']

@admin.register(TotalAssetValue)
class TotalAssetValueAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_value']
    search_fields = ['user__username']