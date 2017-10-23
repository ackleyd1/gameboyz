from django.core.exceptions import PermissionDenied
from allauth.account.forms import LoginForm, SignupForm

class UserMixin:
    """Mixin for Signup and Login on the navbar template."""
    def get_context_data(self, *args, **kwargs):
        context = super(UserMixin, self).get_context_data(*args, **kwargs)
        context['login_form'] = LoginForm()
        context['signup_form'] = SignupForm()
        return context

class IsStaff:
    """Mixin for ensuring only staff members are allowed past this point."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied