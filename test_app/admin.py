from django.contrib import admin

# Register your models here.
from .models import CourseModel, LectureUser

admin.site.register(CourseModel)
admin.site.register(LectureUser)