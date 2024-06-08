from typing import Any

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'landing/index.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        return context
