from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.conf import settings
class CustomLoginRequiredMixin(LoginRequiredMixin):
  permission_denied_message = 'You need to login to access the page'

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      messages.add_message(request, messages.WARNING, settings.MESSAGES['WARNING']['LOGIN_REQUIRED'])
      return self.handle_no_permission()
    return super(CustomLoginRequiredMixin, self).dispatch(
      request, *args, **kwargs)