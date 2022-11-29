from django.apps import AppConfig


class SchedulersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "schedulers"
    def ready(self) -> None:
        from schedulers import apschedulers
        return super().ready()
    

