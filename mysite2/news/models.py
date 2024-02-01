import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin


class Articles(models.Model):
    title = models.CharField("Название", max_length=50)
    anons = models.CharField("Анонс", max_length=250)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/news/{self.id}"

    @admin.display(
        boolean=True,
        ordering="date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date <= now

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
