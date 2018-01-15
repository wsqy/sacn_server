from django.contrib import admin
from scanBase.models import CountryInfo

# Register your models here.
@admin.register(CountryInfo)
class CountryInfoAdmin(admin.ModelAdmin):
    list_display = ('country_cn', 'country_en', 'letter3', 'digital_code')
    list_display_links = ('country_cn', )
