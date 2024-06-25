import uuid

from django.db import models


# Create your models here.

class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    key = models.CharField(max_length=100)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Nav(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=200)
    role = models.ForeignKey(Role, related_name='navs', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.label
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label


class Child(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    key = models.CharField(max_length=100)
    label = models.CharField(max_length=100)
    icon = models.CharField(max_length=200, default='<i className="fa fa-circle-o"></i>')
    role = models.ForeignKey(Role, related_name='nav_child', on_delete=models.CASCADE)
    nav = models.ForeignKey(Nav, related_name='children', on_delete=models.CASCADE)
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.label
        super().save(*args, **kwargs)

    def __str__(self):
        return self.label
