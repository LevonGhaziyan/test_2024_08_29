from django.views import View
from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from ..models import LectureUser

class UserBase(View):
    def render_page(self, *, error=None):
        self.context = {}

        if error:
            self.context["error"] = error

        return render(self.request, self._template, self.context)


class LogIn(UserBase):
    _template = "test_app/log_in.html"

    _success_redirect = "/"

    def get(self, request):
        return self.render_page()

    def post(self, request: HttpRequest):
        self.request = request

        self._get_from_POST()
        self._user_authenticate()

        try:
            login(self.request, self.user)
        except:
            return self.render_page("Login was failed!!")
        
        return HttpResponseRedirect(self._success_redirect)
        
    
    def _get_from_POST(self):
        self.username = self.request.POST.get("username")
        self.password = self.request.POST.get("password")


    def _user_authenticate(self):
        try:
            self.user = authenticate(username=self.username, password=self.password)
        except:
            raise Http404("Something went wrong!!")
    
class LogOut(UserBase):
    _success_redirect = "/login"

    def get(self, request:HttpRequest):
        self.request = request

        logout(request)

        return HttpResponseRedirect(self._success_redirect)



class SignUp(UserBase):
    _template = "test_app/sign_up.html"

    _success_redirect = "/login"

    def get(self, request:HttpRequest):
        self.request = request

        return self.render_page()
    
    def post(self, request:HttpRequest):
        self.request = request

        self._get_from_POST()

        self._create_user()

        self._create_lecture()

        return HttpResponseRedirect(self._success_redirect)

    def _get_from_POST(self):
        self.firstname = self.request.POST.get("firstname", "")
        self.lastname = self.request.POST.get("lastname", "")
        self.age = self.request.POST.get("age", "")
        self.email = self.request.POST.get("email", "")
        self.username = self.request.POST.get("username", "")
        self.password = self.request.POST.get("password", "")

    def _create_user(self):
        try:
            self.user = User.objects.create_user(first_name=self.firstname, last_name=self.lastname, email=self.email, username=self.username, password=self.password)
            
            self.user.save()
        except Exception as e:
            print(e)
            raise Http404("Something went wrong!!")

    def _create_lecture(self):
        try:
            lecture_user = LectureUser(user=self.user, age=self.age)

            lecture_user.save()
        except:
            raise Http404("Something went wrong!!")