from django.apps import AppConfig
from django.db.models.signals import post_migrate


class OrganizationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "organizations"

    def ready(self):
        from organizations.signals import create_company_profile
