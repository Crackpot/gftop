from registration.models import RegistrationProfile
from registration.forms import RegistrationForm

from captcha.fields import CaptchaField

class CaptchaRegistrationForm(RegistrationForm):
    captcha = CaptchaField()
    
    class Meta:
        model = RegistrationProfile
