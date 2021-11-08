from django.db import models
from django.utils import timezone

class FeedBack(models.Model):
    email = models.EmailField(max_length=70, verbose_name='Почта')
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    text = models.TextField(blank=True, verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Обращение'
        verbose_name_plural = 'Обращения'
        ordering = ['-created_date']