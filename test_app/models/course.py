from django.db import models

class CourseModel(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    rate = models.FloatField()
    count = models.IntegerField()
 
    last_update = models.DateTimeField(auto_now=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title