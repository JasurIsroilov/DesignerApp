from django.views.generic import RedirectView
from django.urls import path

from .views import (
    IndexView,
)


urlpatterns = [
    path('', RedirectView.as_view(url='/docs'), name='index-view')
    # path('', IndexView.as_view(), name='index-view'),
]
