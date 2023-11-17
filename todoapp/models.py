from django.db import models


class TodoModel(models.Model):
    title = models.CharField(verbose_name="Title", max_length=122)
    content = models.TextField(verbose_name="Content" )
    anded = models.BooleanField(verbose_name="Ended", default=False)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Updated", auto_now=True)