from django.db import models
from django.utils import timezone


class ShelfAuthor(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        abstract = True


class ShelfObject(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, default="SomeObject")
    status = models.IntegerField(default=0)  # "to do", "in progress" or "done"
    priority = models.IntegerField(default=0)
    # TODO:
    ## add abstract creator field
    description = models.TextField(default="", blank=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        abstract = True


class BookAuthor(ShelfAuthor):
    born = models.DateField()
    died = models.DateField()
    # name =   # should this work?

    def __str__(self):
        return self.title


class BookObject(ShelfObject):
    pub_year = models.DateField()
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE)

    # TODO:
    ## notes should be like (page, the_note) or plain text note?
    ## notes = models. ?

    # TODO:
    ## check all classes for similar fields to move them to general objects

    def __str__(self):
        return self.title + ' - ' + str(self.author)
