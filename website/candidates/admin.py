from django.contrib import admin
from .models import Candidate
from watson.admin import SearchAdmin
    
class CandidateAdmin(SearchAdmin, admin.ModelAdmin):
    exclude = ["slug"] # autoset on save
    ordering = ["candidate_name"]

    search_fields = ["candidate_name"] # for Watson search

admin.site.register(Candidate, CandidateAdmin)