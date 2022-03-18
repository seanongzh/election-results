from django.contrib import admin

from .models import Candidate, ElectedPosition, Election, Party, Result

admin.site.register(Candidate)
admin.site.register(ElectedPosition)
admin.site.register(Election)
admin.site.register(Party)
admin.site.register(Result)
