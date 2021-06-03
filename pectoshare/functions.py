from django.conf import settings

def get_conf_message(type, message):
  return settings.MESSAGES[type][message]