from .forms import CrispyLoginForm, CrispySignupForm

class UserMixin:
    """Mixin for Signup and Login on the navbar template."""
    def get_context_data(self, *args, **kwargs):
        context = super(UserMixin, self).get_context_data(*args, **kwargs)
        context['login_form'] = CrispyLoginForm()
        context['signup_form'] = CrispySignupForm()
        context['user_enabled'] = True
        return context