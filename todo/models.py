from django.db import models


class Todo(models.Model):
    title = models.CharField(verbose_name='タイトル', max_length=30)

    def __str__(self):
        return self.title
