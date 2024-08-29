from abc import ABC, abstractmethod
from typing import Any
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404

class PermissionABC(ABC):
    def decorator(self):
        def decorator_inner(func):
            def wrapper(self_inner, request, *args, **kwargs):
                permission = self.checker(request)
                if permission:
                    return func(self_inner, request, *args, **kwargs)
                else:
                    return self.on_deny()
            
            wrapper.__name__ = decorator_inner.__name__
            wrapper.__doc__ = decorator_inner.__doc__
            return wrapper
        
        decorator_inner.__name__ = self.decorator.__name__
        decorator_inner.__doc__ = self.decorator.__doc__
        return decorator_inner
    
    @abstractmethod
    def checker(self):
        pass
    
    @abstractmethod
    def on_deny(self):
        pass

class LoginRequired(PermissionABC):
    def __call__(self):
        return self.decorator()

    def checker(self, request: HttpRequest):
        return request.user.is_authenticated
    
    def on_deny(self):
        return HttpResponseRedirect("/login")