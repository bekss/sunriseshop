from django.views.generic import ListView
from .models import Tovar


class Content(ListView):
    model = Tovar
    template_name = 'index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = Tovar.objects.filter(amount__gt=0)
        return context


class TovarInfo(ListView):
    model = Tovar
    template_name = 'index.html'
    context_object_name = 'tovar_info'

    def get_queryset(self):
        tovar_info = Tovar.objects.filter(category_tovar__name_category=self.kwargs['slug'], amount__gt=0)
        return tovar_info
























# class Sultan(UserPassesTestMixin, ListView):
#     login_url = 'user_login'
#     model = Sultan
#     model = Vazir
#     queryset = Sultan.objects.all()
#     template_name = 'world/sultan.html'
#
#     def test_func(self):
#         return self.request.user.is_active