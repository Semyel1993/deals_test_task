from django.db import models


class Deal(models.Model):
    customer = models.CharField(
        verbose_name='Логин покупателя',
        max_length=100,
    )
    item = models.CharField(
        verbose_name='Наименование товара',
        max_length=100,
    )
    total = models.PositiveIntegerField(
        verbose_name='Сумма сделки',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество товара, шт',
    )
    date = models.DateTimeField(
        verbose_name='Дата и время регистрации сделки',
    )

    class Meta:
        verbose_name = 'Сделка'
        verbose_name_plural = 'Сделки'

    def __str__(self) -> str:
        return f'{self.customer} - {self.item}'
