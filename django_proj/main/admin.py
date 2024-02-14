from django.contrib import admin

from main.models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
    )


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "name",
        "menu",
        "parent",
        "path",
    )
    list_editable = (
        "name",
        "menu",
        "parent",
        "path",
    )
