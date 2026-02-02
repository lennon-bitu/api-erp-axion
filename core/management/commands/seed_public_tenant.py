from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils.timezone import now
from core.models import Client, Domain  # ajuste o import conforme seu app

User = get_user_model()


class Command(BaseCommand):
    help = 'Seed initial public tenant, domain and superuser'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Starting seed process...'))

        # ==============================
        # Create Public Tenant
        # ==============================
        tenant, created = Client.objects.get_or_create(
            schema_name='public',
            defaults={
                'name': 'Axion Tech.',
                'paid_until': now().date(),
                'on_trial': False,
            }
        )

        if created:
            self.stdout.write(self.style.SUCCESS('Public tenant created'))
        else:
            self.stdout.write(self.style.WARNING('Public tenant already exists'))

        # ==============================
        # Create Domain
        # ==============================
        domain, domain_created = Domain.objects.get_or_create(
            domain='localhost',  # ajuste conforme necessário
            defaults={
                'tenant': tenant,
                'is_primary': True,
            }
        )

        if domain_created:
            self.stdout.write(self.style.SUCCESS('Domain created'))
        else:
            self.stdout.write(self.style.WARNING('Domain already exists'))

        # ==============================
        # Create Superuser
        # ==============================
        admin_username = 'admin'
        admin_email = 'admin@axionapi.com.br'
        admin_password = 'admin123'  # ALTERE EM PRODUÇÃO

        if not User.objects.filter(username=admin_username).exists():
            user = User.objects.create_superuser(
                username=admin_username,
                email=admin_email,
                password=admin_password,
                first_name='Axion',
                last_name='API',
            )

            self.stdout.write(self.style.SUCCESS('Superuser created'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists'))

        self.stdout.write(self.style.SUCCESS('Seed process finished successfully'))
