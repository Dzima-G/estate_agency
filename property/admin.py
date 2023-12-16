from django.contrib import admin

from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.owned_apartments.through
    raw_id_fields = ('owner', 'flat',)


@admin.register(Flat)
class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at', ]
    list_display = ('address', 'price',
                    'new_building',
                    'construction_year',
                    'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ('likes',)
    inlines = [OwnerInline, ]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    raw_id_fields = ('owned_apartments',)
