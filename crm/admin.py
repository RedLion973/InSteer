from django.contrib import admin
from InSteer.crm.models import Country, Company, Department, Client, PhoneNumber
from InSteer.crm.forms import ClientForm

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'city', 'location',]
    list_filter = ['company', 'city',]
    search_fields = ['name',]

class PhoneNumberInline(admin.StackedInline):
    model = PhoneNumber
    extra = 2
    
class ClientAdmin(admin.ModelAdmin):
    form = ClientForm
    inlines = [PhoneNumberInline,]
    list_display = ['human_readable_name', 'department', 'position',]
    list_filter = ['department__company', 'department__name',]
    search_fields = ['user__fist_name', 'user__last_name',]

admin.site.register(Country)
admin.site.register(Company)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Client, ClientAdmin)