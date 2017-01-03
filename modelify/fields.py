from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.timezone import now


class BaseCRUDAtField(models.DateTimeField):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['editable'] = False
        kwargs['null'] = True
        kwargs.setdefault('verbose_name', _('crud at'))

        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        raise NotImplementedError(
            _('pre_save method has to be overridden in child model class.')
        )


class CreatedAtField(BaseCRUDAtField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', _('created at'))
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = now()
        setattr(model_instance, self.attname, value)
        return value


class ReadAtField(BaseCRUDAtField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', _('read at'))
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if add:
            value = None

        setattr(model_instance, self.attname, value)
        return value


class UpdatedAtField(BaseCRUDAtField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', _('updated at'))
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = None
        if not add:
            value = now()

        setattr(model_instance, self.attname, value)
        return value


class DeletedAtField(BaseCRUDAtField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('verbose_name', _('deleted at'))
        super().__init__(*args, **kwargs)

    def pre_delete(self, model_instance):
        value = now()
        setattr(model_instance, self.attname, value)
        return value

    def pre_restore(self, model_instance):
        value = None
        setattr(model_instance, self.attname, value)
        return value

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if add:
            value = None

        setattr(model_instance, self.attname, value)
        return value
