from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=20)


class Format(models.Model):
    name = models.CharField(max_length=20)


class Region(models.Model):
    name = models.CharField(max_length=20)


class Language(models.Model):
    name = models.CharField(max_length=20)


class Profession(models.Model):
    name = models.CharField(max_length=20)


class Category(models.Model):
    name = models.CharField(max_length=20)


class Title(models.Model):
    title_id = models.CharField(max_length=50)
    title_format = models.ForeignKey('Format')
    primary_title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    is_adult = models.BooleanField()
    start_year = models.CharField()
    end_year = models.CharField()
    runtime_minutes = models.IntegerField()
    genres = models.ManyToManyField('Genre')


class TitleAka(models.Model):
    title = models.ForeignKey('Title')
    ordering = models.IntegerField()
    name = models.CharField(max_length=255)
    region = models.ForeignKey('Region')
    language = models.ForeignKey('Language')
    ttypes = models.CharField(max_length=10)
    attributes = models.CharField(max_length=255)
    is_original_title = models.BooleanField()


class Person(models.Model):
    person_id = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    death_year = models.IntegerField()
    professions = models.ManyToManyField('Profession')
    titles = models.ManyToManyField('Title')


class Crew(models.Model):
    title = models.ForeignKey('Title')
    directors = models.ManyToManyField('Person')
    writers = models.ManyToManyField('Writers')


class Principal(models.Model):
    title = models.ForeignKey('Title')
    ordering = models.IntegerField()
    person = models.ForeignKey('Person')
    category = models.ForeignKey('Category')
    job = models.CharField(max_length=255)
    characters = models.CharField(max_length=255)


class Rating(models.Model):
    title = models.ForeignKey('Title')
    avg_rating = models.IntegerField()
    number_of_votes = models.IntegerField()


class Episode(models.Model):
    title = models.ForeignKey('Title')
    parent_title = models.ForeignKey('Title')
    season_number = models.IntegerField()
    episode_number = models.IntegerField()


