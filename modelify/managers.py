from django.db import models
from django.utils.timezone import now


class DeletedQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted_at=now())

    def restore(self):
        self.update(deleted_at=None)


class DeletedManager(models.Manager):
    def get_queryset(self):
        return DeletedQuerySet(self.model, using=self._db).filter(
            deleted_at=None
        )

    @property
    def deleted(self):
        return DeletedQuerySet(self.model, using=self._db).filter(
            deleted_at__isnull=False
        )
