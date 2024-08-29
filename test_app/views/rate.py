from django.views import View
from django.http import HttpRequest, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404

from ..models import CourseModel
from .permissions import LoginRequired

class RateBase(View):
    def _get_course(self):
        self.course = get_object_or_404(CourseModel, pk=self.course_number)

class RateView(RateBase):
    _template = "test_app/rate.html"

    @property
    def _success_redirect(self):
        return f"/course/{self.course_number}"

    @LoginRequired()()
    def get(self, request: HttpRequest, course_number):
        self.request = request
        self.course_number = course_number

        self._get_course()

        context = {"course": self.course}
        return render(self.request, self._template, context)

    @LoginRequired()()
    def post(self, request: HttpRequest, course_number):
        self.request = request
        self.course_number = course_number

        self._get_course()

        self._get_from_POST()

        self._save_rate()

        return HttpResponseRedirect(self._success_redirect)
    
    def _get_from_POST(self):
        self.new_rate = self.request.POST.get("rate", "")

    def _save_rate(self):
        try:
            self.course.rate = (self.course.rate * self.course.count + float(self.new_rate)) / (self.course.count + 1)
            self.course.save()
        except:
            raise Http404("Something went wrong!!")