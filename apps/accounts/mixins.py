from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.contrib import messages
from pectoshare.functions import get_conf_message

class CustomLoginRequiredMixin(LoginRequiredMixin):
  permission_denied_message = get_conf_message('WARNING', 'LOGIN_REQUIRED')

  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_authenticated:
      messages.add_message(request, messages.WARNING, self.permission_denied_message)
      return self.handle_no_permission()
    return super(CustomLoginRequiredMixin, self).dispatch(
      request, *args, **kwargs)

class ObjectAccessPermissionMixin(AccessMixin):
  permission_denied_message = get_conf_message('WARNING', 'PERMISSION_DENIED')

  def dispatch(self, request, *args, **kwargs):
    instance = self.get_object()
    instance_owner = instance.user 
    if request.user != instance_owner:
      messages.add_message(request, messages.WARNING, self.permission_denied_message)
      return self.handle_no_permission()
    return super(ObjectAccessPermissionMixin, self).dispatch(request, *args, **kwargs)
