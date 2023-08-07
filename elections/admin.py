from django.contrib import admin
from .models import Election
from results.models import Result

class ResultInline(admin.TabularInline):
    model = Result
    extra = 1
    fieldsets = [
        ("Candidate details", {"fields": [("candidate", "party")]}),
        ("Candidate results", {"fields": [("votes", "candidate_is_incumbent", "candidate_is_winner")]}),
    ]
    autocomplete_fields = ["candidate"]
    
class ElectionAdmin(admin.ModelAdmin):
    exclude = ["slug"] # autoset on save
    fieldsets = [
        ("Election details", {"fields": ["year", ("position", "is_special")]})
    ]
    inlines = [ResultInline]

admin.site.register(Election, ElectionAdmin)