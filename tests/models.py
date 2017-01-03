from django.db import models
from django.utils.translation import ugettext_lazy as _

from modelify import mixins


class BasePerson(models.Model):
    class _Default:
        first_name = _('John')
        last_name = _('Doe')
        age = 23

    class Meta:
        app_label = 'tests'
        abstract = True

    first_name = models.CharField(
        default=_Default.first_name,
        max_length=64,
        verbose_name=_('first name'),
    )

    last_name = models.CharField(
        default=_Default.last_name,
        max_length=64,
        verbose_name=_('last name'),
    )

    age = models.PositiveSmallIntegerField(
        default=_Default.age,
        verbose_name=_('age'),
    )


class PersonCreatedAt(mixins.CreatedAtMixin, BasePerson):
    pass


class PersonUpdatedAt(mixins.UpdatedAtMixin, BasePerson):
    pass


class PersonSoftDelete(mixins.SoftDeleteMixin, BasePerson):
    pass
