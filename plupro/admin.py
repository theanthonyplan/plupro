from django.contrib import admin
from .models import Proposal, ProposalLine, ProposalLineCategory, ProposalLineItem

class ProposalLineItemTabularInline(admin.TabularInline):
    model = ProposalLineItem
    extra = 1


class ProposalLineTabularInline(admin.TabularInline):
    model = ProposalLine
    inlines = [ProposalLineItemTabularInline]
    extra = 1
    ordering = ['quantity', 'override','proposal']


class ProposalLineItemAdmin(admin.ModelAdmin):
    model = ProposalLineItem
    # list_display = ['quantity', 'category','override','proposal']


class ProposalLineAdmin(admin.ModelAdmin):
    model = ProposalLine
    list_display = ['quantity', 'override','proposal', ]


class ProposalAdmin(admin.ModelAdmin):
    inlines = [ProposalLineTabularInline]
    model = Proposal

class ProposalLineCategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalLine, ProposalLineAdmin)
admin.site.register(ProposalLineCategory, ProposalLineCategoryAdmin)
admin.site.register(ProposalLineItem, ProposalLineItemAdmin)
