from tortoise import fields
from tortoise.models import Model


class Author(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    bio = fields.TextField(null=True)
    books = fields.ReverseRelation['Book']

    def __str__(self):
        return self.name


class Book(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    author = fields.ForeignKeyField('models.Author', related_name='books')
    published_date = fields.DateField(null=True)
    description = fields.TextField(null=True)

    def __str__(self):
        return self.title


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, unique=True)
    password = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)

    def __str__(self):
        return self.username
