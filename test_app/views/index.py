from django.views import View
from django.http import HttpRequest
from django.shortcuts import render

from ..models import CourseModel

class IndexView(View):
    _template = "test_app/index.html"

    def get(self, request: HttpRequest):
        courses = CourseModel.objects.all()
        context = {"courses": courses}
        return render(request, self._template, context)