from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from mysite.accounts.forms import CaptchaRegistrationForm
from mysite.settings import USE_CAPTCHA

if USE_CAPTCHA:
    register_args = {'form_class':CaptchaRegistrationForm}
else:
    register_args = {}

urlpatterns = patterns('',
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout', {'next_page':'/'}),
    
    (r'^register/$', 'registration.views.register', register_args),
    (r'^activate/(?P<activation_key>\w+)/$', 'registration.views.activate'),
    url(r'^register/complete/$',
                direct_to_template,
                {'template': 'registration/registration_complete.html'},
                name='registration_complete')
)