from django.conf.urls.defaults import patterns
from django.views.generic import ListView
from InSteer.ownership.models import Project

urlpatterns = patterns('',
    (r'^projects/$', ListView.as_view(
        model=Project,
    )),
)