from django.db.models import Count

from .models import *

menu = [{'title': "Таблица", 'url_name': 'words'},
        {'title': "Тест", 'url_name': 'test'},
        ]


class DataMixin:


    def get_user_context(self, **kwargs):
        context = kwargs

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(0)
            user_menu.pop(0)         #убирает в меню поля

        context['menu'] = user_menu

        return context




