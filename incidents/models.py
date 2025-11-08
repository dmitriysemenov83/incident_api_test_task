from django.db import models


class IncidentStatus(models.TextChoices):
    OPEN = 'open', 'Открыта'
    IN_PROGRESS = 'in_progress', 'В работе'
    RESOLVED = 'resolved', 'Решена'
    CLOSED = 'closed', 'Закрыта'


class IncidentSource(models.TextChoices):
    OPERATOR = 'operator', 'Оператор'
    MONITORING = 'monitoring', 'Мониторинг'
    PARTNER = 'partner', 'Партнер'


class Incident(models.Model):
    description = models.TextField(verbose_name='Описание')
    status = models.CharField(
        max_length=20,
        choices=IncidentStatus.choices,
        default=IncidentStatus.OPEN,
        verbose_name='Статус'
    )
    source = models.CharField(
        max_length=20,
        choices=IncidentSource.choices,
        default=IncidentSource.MONITORING,
        verbose_name='Источник'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        verbose_name = 'Инцидент'
        verbose_name_plural = 'Инциденты'
        ordering = ['-created_at']
        db_table = 'incidents'

    def __str__(self):
        return f"{self.id} - {self.status}"
