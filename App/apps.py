#Importaciones------------------------------
from django.apps import AppConfig

#Code---------------------------------
class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App'
