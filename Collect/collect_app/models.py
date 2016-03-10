from django.db import models

class Information(models.Model):
    name = models.TextField()
    num = models.TextField()
    email = models.EmailField()
    def __str__(self):
        return (str(self.id) + ": " + self.name)