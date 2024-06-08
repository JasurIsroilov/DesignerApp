from django.contrib import admin

from .models import (
    DocumentsModel,
    DocumentCategoriesModel,
    DynamicFormModel,
    DocsFormLinkModel,
)


@admin.register(DynamicFormModel)
class DynamicFormAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['field_validator'].required = False
        form.base_fields['field_class'].required = False
        return form


@admin.register(DocsFormLinkModel)
class DocsFormLinkAdmin(admin.ModelAdmin):
    ...


@admin.register(DocumentsModel)
class DocumentsAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['name'].required = False
        return form


@admin.register(DocumentCategoriesModel)
class DocsStructureAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['parent'].required = False
        form.base_fields['level'].required = False
        return form
