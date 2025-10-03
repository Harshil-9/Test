from django.db import models
from django.conf import settings

class Project(models.Model):
    name = models.CharField(max_length=200)
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, limit_choices_to={"role":"PM"})
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="projects", limit_choices_to={"role":"EMPLOYEE"})
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
