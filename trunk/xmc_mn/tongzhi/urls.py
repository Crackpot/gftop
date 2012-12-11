from django.conf.urls import url, patterns
from django.views.generic.detail import DetailView
from tongzhi.models import Tongzhi
urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Tongzhi,
            template_name='tongzhi/detail.html')),
)
