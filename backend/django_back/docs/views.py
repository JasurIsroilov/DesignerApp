from django.views.generic import (
    ListView,
    View,
)
from django.shortcuts import render

from .models import DocumentCategoriesModel
from docs.services import get_tree_structure


class DocsListView(ListView):
    template_name = 'docs/docs_list.html'
    model = DocumentCategoriesModel
    context_object_name = 'tree'
    extra_context = {
        'title': 'Список документов'
    }

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hierarchy'] = get_tree_structure()
        return context


class ModalFormView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request,
                      template_name='docs/forms/modal_form.html',
                      context=context)
