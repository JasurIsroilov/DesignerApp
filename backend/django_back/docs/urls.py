from django.urls import path

from .views import (
    DocsListView,
    ModalFormView,
)


urlpatterns = [
    path('', DocsListView.as_view(), name='docs-list'),
    path('modal-form/', ModalFormView.as_view(),
         name='docs-modal-form'),
]
