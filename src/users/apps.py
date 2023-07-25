from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        from users.signals import create_group

    #
    # def ready(self):
    #     from users.signals import create_profile, save_profile