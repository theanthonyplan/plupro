from django.contrib import admin
from .models import Proposal, ProposalLine, ProposalLineCategory

class ProposalLineTabularInline(admin.TabularInline):
    model = ProposalLine

class ProposalLineAdmin(admin.ModelAdmin):
    model = ProposalLine
    list_display = ['quantity', 'override', 'category','proposal']


class ProposalAdmin(admin.ModelAdmin):
    inlines = [ProposalLineTabularInline]
    model = Proposal

class ProposalLineCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalLine, ProposalLineAdmin)
admin.site.register(ProposalLineCategory, ProposalLineCategoryAdmin)
