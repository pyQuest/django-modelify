import datetime

from django.test import TestCase

from . import models

# TODO: Test interactions - should deleting an object also modify updated_at?


class TestCreatedAtMixin(TestCase):
    def setUp(self):
        self.person = models.PersonCreatedAt.objects.create()

    def test_is_person_object_in_db(self):
        db_person = models.PersonCreatedAt.objects.get(pk=self.person.pk)
        assert db_person == self.person

    def test_person_contains_valid_created_at(self):
        assert hasattr(self.person, 'created_at')
        assert isinstance(self.person.created_at, datetime.datetime)


class TestUpdatedAtMixin(TestCase):
    def setUp(self):
        self.person = models.PersonUpdatedAt.objects.create()

    def test_is_person_object_in_db(self):
        db_person = models.PersonUpdatedAt.objects.get(pk=self.person.pk)
        assert db_person == self.person

    def test_person_contains_null_updated_at(self):
        assert hasattr(self.person, 'updated_at')
        assert self.person.updated_at is None

    def test_update_person_modifies_updated_at(self):
        self.person.first_name = 'Quentin'
        self.person.last_name = 'Tarantino'
        self.person.save()

        db_person = models.PersonUpdatedAt.objects.get(pk=self.person.pk)
        assert isinstance(db_person.updated_at, datetime.datetime)


class TestSoftDeleteMixin(TestCase):
    def setUp(self):
        self.person = models.PersonSoftDelete.objects.create()
        self.people_pk = [
            person.pk for person in [
                models.PersonSoftDelete.objects.create(),
                models.PersonSoftDelete.objects.create(),
            ]
       ]

    def test_is_person_object_in_db(self):
        db_person = models.PersonSoftDelete.objects.get(pk=self.person.pk)
        assert db_person == self.person

    def test_person_contains_null_deleted_at(self):
        assert hasattr(self.person, 'deleted_at')
        assert self.person.deleted_at is None

    def test_person_update_does_not_modify_deleted_at(self):
        self.person.first_name = 'Quentin'
        self.person.last_name = 'Tarantino'
        self.person.save()

        assert self.person.deleted_at is None

    def test_soft_delete_modifies_deleted_at(self):
        self.person.delete()

        db_person = models.PersonSoftDelete.objects.deleted.get(pk=self.person.pk)
        assert isinstance(db_person.deleted_at, datetime.datetime)

    def test_soft_delete_modifies_queryset_deleted_at(self):
        print(self.people_pk)
        models.PersonSoftDelete.objects.filter(pk__in=self.people_pk).delete()

        db_people = models.PersonSoftDelete.objects.deleted.filter(
            pk__in=self.people_pk
        )
        assert db_people.count() == len(self.people_pk)

        for person in db_people:
            assert isinstance(person.deleted_at, datetime.datetime)
