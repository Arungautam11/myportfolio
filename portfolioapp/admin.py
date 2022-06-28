from django.contrib import admin
from portfolioapp.models import Portfolio, Contact


# Register your models here.


class ContactAdmin(admin.ModelAdmin):
	list_display=('name', 'phone', 'email', 'subject')
	list_filter=('name', 'subject')

admin.site.register(Portfolio)
admin.site.register(Contact, ContactAdmin)

