from django.contrib import admin
from .models import CompanyDetail, CompanyTests, Tests, OrderInfo,  Company # ,CompanyLogin

admin.site.register(CompanyDetail)
admin.site.register(Tests)
admin.site.register(CompanyTests)
admin.site.register(OrderInfo)
admin.site.register(Company)
# admin.site.register(CompanyLogin)