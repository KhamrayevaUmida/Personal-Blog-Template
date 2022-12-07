from django.db import models

class Post(models.Model):
    name = models.CharField('Nomi', max_length=255)
    content = models.TextField('mazmun',)
    tanlov = models.CharField('tanlov', max_length=20)
    date = models.DateTimeField('Vaqt', auto_now_add=True)
    image = models.CharField('rasm', max_length=255)

    def __str__(self):
        return self.name


class TopPost(models.Model):
    name = models.CharField("Nomi", max_length=255)
    tanlov = models.CharField('tanlov', max_length=20)
    date = models.DateTimeField('vaqt',auto_now_add=True)
    image = models.CharField('rasm', max_length=255)

    def __str__(self):
        return self.name


class NextPost(models.Model):
    name = models.CharField('Nomi', max_length=255)
    content = models.TextField('mazmun',)
    tanlov = models.CharField('tanlov', max_length=20)
    date = models.DateTimeField('Vaqt', auto_now_add=True)
    image = models.CharField('rasm', max_length=255)

    def __str__(self):
        return self.name