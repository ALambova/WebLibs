from django.db import models
import uuid


class Book(models.Model):
    #GENRES =
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    rating = models.FloatField(default=0)
    review = models.TextField(blank=True)
    #genre = models.CharField(choices=GENRES)
    #ISBN = models.CharField(max_length=20, blank=True)


class BookEntity(models.Model):
    unique_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, null=True)
