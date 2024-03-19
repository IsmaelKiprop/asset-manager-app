from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib import admin
from .models import *

class CustomUserAdmin(UserAdmin):
  list_display = ('email', 'is_staff', 'is_superuser')
  ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)  # Register your custom user model with the Django admin



#@admin.register(IntangibleAssetIndustry)
#class IntangibleAssetIndustryAdmin(admin.ModelAdmin):
#    list_display = ['name']
#    pass#
#@admin.register(IntangibleAssetCategory)
#class IntangibleAssetCategoryAdmin(admin.ModelAdmin):
#    list_display = ['name', 'industry']
#    #
#@admin.register(IntangibleAsset)
#class IntangibleAssetAdmin(admin.ModelAdmin):
#    list_display = ['name','category', 'date_registered', 'expiring_date', 'value', 'owner','date_created', 'date_modified']
#    list_filter = ['category', 'owner',
#     'date_created', 'date_modified']
#    search_fields = ['name', 'owner__username']
#    date_hierarchy = 'date_created'#
#@admin.register(AssetDocument)
#class AssetDocumentAdmin(admin.ModelAdmin):
#    list_display = ['asset', 'description'] 
#    search_fields = ['asset__name'] 
#    #
#@admin.register(ConcernedPeople)
#class ConcernedPeopleAdmin(admin.ModelAdmin):
#    #list_display = ['asset','name', 'title', 'contact_details']
#    search_fields = ['asset__name']
#    #
#@admin.register(ExpiringAsset)
#class ExpiringAssetAdmin(admin.ModelAdmin):
#    list_display = ['asset','notification_date', 'notified']
#    list_filter = ['notification_date', 'notified']
#    search_fields = ['asset__name']#
#@admin.register(TotalAssetValue)
#class TotalAssetValueAdmin(admin.ModelAdmin):
#    list_display = ['user','total_value']
#    search_fields = ['user__username']#
#@admin.register()  

admin.site.register(AuthToken) 
admin.site.register(Company) 
admin.site.register(ChatMessage) 
admin.site.register(Currency)
admin.site.register(Valuation)
admin.site.register(Asset)  
admin.site.register(InventoryItem)  
admin.site.register(Expense)
admin.site.register(Invoice)
admin.site.register(BankConnection)
admin.site.register(VAT)
admin.site.register(Report)
admin.site.register(Employee)
admin.site.register(Transaction)
admin.site.register(Inventory)
admin.site.register(Project)
admin.site.register(Warehouse)
admin.site.register(StockReturn)
admin.site.register(StockRequest)
admin.site.register(Savings)
admin.site.register(Budget)  
admin.site.register(BankIntegration)
admin.site.register(Bill)
admin.site.register(Analytics)
admin.site.register(AssetsValuation)
admin.site.register(CreditScore)
admin.site.register(CustomizableAlert)
admin.site.register(FinancialGrowth)
admin.site.register(CheckingAccount)
admin.site.register(Insurance)
admin.site.register(Investing)
admin.site.register(AccountingSoftwareIntegration)
admin.site.register(IntangibleAssetIndustry) 
admin.site.register(IntangibleAssetCategory) 
admin.site.register(IntangibleAsset) 
admin.site.register(AssetDocument) 
admin.site.register(ConcernedPeople) 
admin.site.register(ExpiringAsset) 
admin.site.register(TotalAssetValue) 
admin.site.register(ComputerSoftware) 
admin.site.register(SoftwareDocument) 
admin.site.register(ComputerHardware) 
admin.site.register(HardwareDocument) 
admin.site.register(Machinery) 
admin.site.register(MachineryDocument) 
admin.site.register(Investment)   
admin.site.register(Furniture)  
admin.site.register(FurnitureDocument)  
admin.site.register(FurnitureQRCode)  
admin.site.register(InvestmentDocument)  
admin.site.register(InvestmentConcernedPeople)  
admin.site.register(InvestmentPurchaseRecord) 
admin.site.register(WarrantyRecord)  
admin.site.register(RepairRecord)  
admin.site.register(ServiceRecord)  
admin.site.register(PurchaseRecord)  
admin.site.register(BarcodeScanner)
admin.site.register(QRCodeScanner)  
admin.site.register(RFIDTag)  
admin.site.register(IOTDevice)  
admin.site.register(FixedAsset)  
admin.site.register(FixedAssetDocument)  
admin.site.register(FixedAssetConcernedPeople)  
admin.site.register(LeaseRecord)    
admin.site.register(ContractDocument)  
admin.site.register(Vehicle)  
admin.site.register(VehicleDocument)   
admin.site.register(AssetTransaction) 








