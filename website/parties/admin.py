from django.contrib import admin
from .models import Party

class PartyAdmin(admin.ModelAdmin):
    exclude = ["slug"] # autoset on save

admin.site.register(Party, PartyAdmin)