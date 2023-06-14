from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    email = models.CharField(max_length=30)


class Score(models.Model):
    english = models.CharField(max_length=3)
    math = models.CharField(max_length=3)
    science = models.CharField(max_length=3)
    exam_date = models.DateTimeField()

    student = models.ForeignKey(
        Students, on_delete=models.CASCADE, related_name='score_set')
