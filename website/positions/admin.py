from django.contrib import admin
from .models import Position

class PositionAdmin(admin.ModelAdmin):
    exclude = ["slug"] # autoset on save

admin.site.register(Position, PositionAdmin)