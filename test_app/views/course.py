from django.views import View
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404

from ..models import CourseModel

class CourseView(View):
    _template = "test_app/course.html"

    def get(self, request: HttpRequest, course_number):
        course = get_object_or_404(CourseModel, pk=course_number)

        context = {"course": course}
        return render(request, self._template, context)