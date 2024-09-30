from django.db import models

# Create your models here.
class question(models.Model):
    year_in_college = {
        "1": "1st Year",
        "2": "2nd Year",
        "3": "3rd Year",
        "4": "4th Year",
    }
    courses = {
        "cse": "cyber security",
        "iot": "internet of things",
        "ai": "Artificial Intelligence & data science",
    }
    name = models.CharField(max_length=100, null=True, blank=True, default="Anonymous")
    course = models.CharField(max_length=3, choices=courses, null=True, blank=True)
    year = models.CharField(max_length=1, choices=year_in_college, null=True, blank=True)
    question_text = models.CharField(max_length=500)
    def __str__(self):
        return self.question_text