from django.db import models

class Shortener(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    long_url = models.URLField()
    short_url = models.CharField(max_length=15, unique=True, blank=True)

    def __str__(self):
        return self.short_url