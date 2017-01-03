from django.db import models
from django.utils.timezone import now

from . import fields
from . import managers


class CreatedAtMixin(models.Model):
    class Meta:
        abstract = True

    created_at = fields.CreatedAtField()


class ReadAtMixin(models.Model):
    class Meta:
        abstract = True

    read_at = fields.ReadAtField()


class UpdatedAtMixin(models.Model):
    class Meta:
        abstract = True

    updated_at = fields.UpdatedAtField()


class SoftDeleteMixin(models.Model):
    class Meta:
        abstract = True

    objects = managers.DeletedManager()

    deleted_at = fields.DeletedAtField()

    def delete(self, using=None, keep_parents=False):
        self._meta.get_field('deleted_at').pre_delete(self)
        self.save(using=None)

    def restore(self):
        self._meta.get_field('deleted_at').pre_restore(self)
        self.save(using=None)


class CreatedReadAtMixin(CreatedAtMixin, ReadAtMixin):
    class Meta:
        abstract = True


class CreatedReadUpdatedAtMixin(CreatedAtMixin, ReadAtMixin, UpdatedAtMixin):
    class Meta:
        abstract = True


class CRUDAtMixin(CreatedReadUpdatedAtMixin, SoftDeleteMixin):
    class Meta:
        abstract = True
