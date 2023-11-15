from django.db import models

class Group(models.Model):
    # id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # members = models.ManyToManyField('self', symmetrical=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

