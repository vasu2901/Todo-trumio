from django.db import models

# Create yocur models here.
class User(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"{self.name}"

class Todo(models.Model):
    title = models.CharField(max_length=256)
    user_id = models.ManyToManyField(User,)
    timestamp = models.DateTimeField()
    status = models.BooleanField()
    def __str__(self) -> str:
        return f"{self.title} - {self.status} - {self.timestamp} - {self.user_id}"
