from django.shortcuts import render, redirect
from . forms import BookForm
from . forms import GenreForm
from . forms import PersonForm
from . forms import GroupForm
from . forms import MembershipForm
from . models import Band

# Create your views here.


def base(request):
    return render(request, 'core/base.html')


def home(request):
    return render(request, 'core/home.html')


def tabela(request):
    return render(request, 'core/tabela.html')


def book(request):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book')
    else:
        form = BookForm()
    return render(request, 'core/book.html', {'form': form})


def genre(request):
    if request.POST:
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre')
    else:
        form = GenreForm()
    return render(request, 'core/genre.html', {'form': form})


def person(request):
    if request.POST:
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('person')
    else:
        form = PersonForm()
    return render(request, 'core/person.html', {'form': form})


def group(request):
    if request.POST:
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group')
    else:
        form = GroupForm()
    return render(request, 'core/group.html', {'form': form})


def membership(request):
    if request.POST:
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership')
    else:
        form = MembershipForm()
    return render(request, 'core/membership.html', {'form': form})


def band_listing(request):
    """ A view of all bands. """
    bands = Band.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        bands = bands.filter(name__icontains=var_get_search)
    return render(request, 'core/band_listing.html', {'bands': bands})
