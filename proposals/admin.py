from django.contrib import admin
# Register your models here.
from .models import Proposal, ProposalLine
from products.models import Product
from products.admin import ProductAdmin, ProductTabularInline

class ProposalLineTabularInline(admin.TabularInline):
    model = ProposalLine
    inlines = [ProductTabularInline]
    extra = 1
    ordering = ['quantity', 'override','proposal']




class ProposalLineAdmin(admin.ModelAdmin):
    model = ProposalLine
    list_display = ['quantity', 'override','proposal', ]


class ProposalAdmin(admin.ModelAdmin):
    inlines = [ProposalLineTabularInline]
    model = Proposal

# class ProposalLineCategoryAdmin(admin.ModelAdmin):
#     pass

admin.site.register(Proposal, ProposalAdmin)
admin.site.register(ProposalLine, ProposalLineAdmin)
# admin.site.register(ProposalLineCategory, ProposalLineCategoryAdmin)
