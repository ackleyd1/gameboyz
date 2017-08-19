from django.core.exceptions import PermissionDenied

from .forms import CrispyLoginForm, CrispySignupForm


class UserMixin:
    """Mixin for Signup and Login on the navbar template."""
    def get_context_data(self, *args, **kwargs):
        context = super(UserMixin, self).get_context_data(*args, **kwargs)
        context['login_form'] = CrispyLoginForm()
        context['signup_form'] = CrispySignupForm()
        context['user_enabled'] = True
        return context

class IsStaff:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_staff:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied