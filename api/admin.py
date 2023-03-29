from django.contrib import admin
from api.models import *


# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Account._meta.fields]
    search_fields = list([field.name for field in Account._meta.fields])

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class SocialAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Social._meta.fields]
    search_fields = list([field.name for field in Social._meta.fields])

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

class PortfolioAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Portfolio._meta.fields]
    search_fields = list([field.name for field in Portfolio._meta.fields])

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class CalendarAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Calendar._meta.fields]
    search_fields = list([field.name for field in Calendar._meta.fields])

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in CompanyInfo._meta.fields]
    search_fields = list([field.name for field in CompanyInfo._meta.fields])

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class AppearanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Appearance._meta.fields]
    search_fields = list([field.name for field in Appearance._meta.fields])

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
class CardAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Card._meta.fields]
    search_fields = list([field.name for field in Card._meta.fields])

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Card, CardAdmin)
admin.site.register(Appearance, AppearanceAdmin)
admin.site.register(CompanyInfo, CompanyInfoAdmin)
admin.site.register(Calendar, CalendarAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Social, SocialAdmin)
admin.site.register(Account, AccountAdmin)