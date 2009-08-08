from django.core.management.base import NoArgsCommand
from registration.models import RegistrationProfile

class Command(NoArgsCommand):
    help = "Execute cron maintenance tasks"
    
    def handle_noargs(self, **options):
        # Delete expired user registrations from the database
        RegistrationProfile.objects.delete_expired_users()
        
        