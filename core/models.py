from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):

    name = models.CharField('Nome', max_length=100)
    genre = models.ManyToManyField(Genre)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['name']

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField('Pessoa', max_length=50)

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['name']

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField('Grupo', max_length=128)
    members = models.ManyToManyField(
        Person,
        through='Membership',
        through_fields=('group', 'person'),
    )

    class Meta:
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'
        ordering = ['name']

    def __str__(self):
        return self.name


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="membership_invites",
    )
    invite_reason = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Membro'
        verbose_name_plural = 'Membros'
        ordering = ['group']

    def __str__(self):
        return self.group


class Band(models.Model):

    """A model of a rock band."""
    name = models.CharField(max_length=200)
    can_rock = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'band'
        verbose_name_plural = 'bands'

    def __str__(self):
        return self.name

    # count members by band
    def get_members_count(self):
        return self.band.count()

    def get_band_detail_url(self):
        return u"/bands/%i" % self.id


class Member(models.Model):

    """A model of a rock band member."""
    name = models.CharField("Member's name", max_length=200)
    instrument = models.CharField(choices=(
        ('g', "Guitar"),
        ('b', "Bass"),
        ('d', "Drums"),
        ('v', "Vocal"),
        ('p', "Piano"),
    ),
        max_length=1
    )

    band = models.ForeignKey("Band",on_delete=models.PROTECT, related_name='band')

    class Meta:
        ordering = ['name']
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        return self.name
