from django.core.management.base import NoArgsCommand

from mysite.settings import *
from mysite.items.models import Item

class Command(NoArgsCommand):
    help = "Init the DB"
    
    def handle_noargs(self, **options):
        # Set superuser
        from django.contrib.auth.models import User
        User.objects.create_superuser(SUPER_USER_NAME, SUPER_USER_EMAIL, SUPER_USER_PASSWORD)
        
        # Add a dummy user
        User.objects.create_user('dummy', 'dummy@test.com', 'dummy')
        
        # Set site data
        from django.contrib.sites.models import Site
        site = Site.objects.get_current()
        site.domain = SITE_URL
        site.name = SITE_NAME
        site.save()
        
        # Some dummy items
        data = {
            'First Item': 'black, white',
            'Second Item': 'red, blue',
            'Third Item': 'gree, white'
        }
        for name, tags in data.items():
            item = Item(name=name)
            item.save()
            item.tags = tags
            
        