from django.views.generic import TemplateView
from InSteer.ownership.models import Project

class HomeView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'projects_list': Project.objects.all()
        })
        return context