from functools import wraps
from django.http import HttpResponseForbidden

def check_permission(permission):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if request.user.has_perm(permission):
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this resource.")
        return _wrapped_view
    return decorator
