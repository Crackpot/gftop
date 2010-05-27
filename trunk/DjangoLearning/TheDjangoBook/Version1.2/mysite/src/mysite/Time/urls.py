from django.conf.urls.defaults import *
from mysite.Time.views import current_datetime, hours_ahead
urlpatterns = patterns('',
    (r'^$', current_datetime),
    (r'^plus/(\d{1,2})/$', hours_ahead),
)
