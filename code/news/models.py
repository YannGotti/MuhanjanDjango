from django.utils import timezone
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    image = models.TextField(
        db_column='image64',
        blank=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-date']
