from django.db import models
from django.utils.translation import gettext as _


from django.utils.translation import gettext as _

class Product(models.Model):
    name = models.CharField(
        max_length=125,
        verbose_name=_('имя')
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name=_('цена')
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('описание')
    )
    collection = models.IntegerField(
        choices=(
            (1, _('Авторские букеты')),
            (2, _('Любимой')),
            (3, _('Маме'))
        )
    )
    quantity = models.IntegerField(verbose_name=_('количество'))
    rating = models.IntegerField(
        default=10,
        verbose_name=_('рейтинг')
    )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')
