from django.apps import AppConfig


class OctofitTrackerConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "octofit_tracker"

    def ready(self):
        print('Debug: octofit_tracker app is ready and initialized.')
