from django.contrib import admin

from menu.models import Menu, MenuItem


class MenuItemAdmin(admin.TabularInline):
    model = MenuItem
    extra = 1


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuItemAdmin]
