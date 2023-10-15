from django.db import models

# Create your models here.

class UniversityCampus(models.Model):
    campus = models.CharField(max_length=60, default="", blank=True, null=False)
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campus_ID = models.IntegerField(default="", blank=True, null=False)

    def __str__(self):
        return self.campus

    class Meta:
        verbose_name_plural = "Unviersity Campus"