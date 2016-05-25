from django.db import models
from django.contrib.auth.models import AbstractUser
from books.models import Book, BookEntity


class CustomUser(AbstractUser):
    address = models.CharField(max_length=50)
    phoneNum = models.CharField(max_length=15)


class LibUser(CustomUser):
    books = models.ManyToManyField(BookEntity, blank=True)
    history = models.ManyToManyField(Book, blank=True)

    class Meta:
        verbose_name = 'LibUser'


class Library(CustomUser):
    director = models.CharField(max_length=50)
    otherInf = models.TextField(max_length=500, blank=True)
    users = models.ManyToManyField(LibUser, blank=True)
    books = models.ManyToManyField(BookEntity, blank=True)

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'


# Create your models here.
