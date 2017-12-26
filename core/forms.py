from django import forms
from . models import Book, Genre, Person, Group, Membership


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name', 'genre',)


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name',)


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'members',)


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ('group', 'person', 'inviter', 'invite_reason',)
