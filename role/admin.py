from django.contrib import admin
from .models import *


# Register your models here.

class ChildInline(admin.TabularInline):
    model = Child
    extra = 1
    exclude = ('key',)


class NavInline(admin.TabularInline):
    model = Nav
    extra = 1
    exclude = ('key',)
    inlines = [ChildInline]


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'label')
    search_fields = ('title', 'label',)
    readonly_fields = ('key',)
    inlines = [NavInline]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not obj:
            fields = [f for f in fields if f != 'key']
        return fields

    def save_model(self, request, obj, form, change):
        if not obj.key:
            obj.key = obj.label
        obj.save()


@admin.register(Nav)
class NavAdmin(admin.ModelAdmin):
    list_display = ('label', 'icon', 'role')
    list_filter = ('role',)
    search_fields = ('label', 'icon')
    readonly_fields = ('key',)
    exclude = ('key',)
    inlines = [ChildInline]

    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if not obj:
            fields = [f for f in fields if f != 'key']
        return fields

    def save_model(self, request, obj, form, change):
        if not obj.key:
            obj.key = obj.label
        obj.save()

#
# @admin.register(Child)
# class ChildAdmin(admin.ModelAdmin):
#     list_display = ('label', 'role', 'nav', 'content')
#     list_filter = ('role', 'nav')
#     search_fields = ('label', 'content')
#     readonly_fields = ('key',)
#
#     def get_fields(self, request, obj=None):
#         fields = super().get_fields(request, obj)
#         if not obj:
#             fields = [f for f in fields if f != 'key']
#         return fields
#
#     def save_model(self, request, obj, form, change):
#         if not obj.key:
#             obj.key = obj.label
#         obj.save()
