from django.shortcuts import render, get_object_or_404
from .models import Band, Member
from django.http import HttpResponse

from django_tables2 import RequestConfig
from .tables import BandTable, MemberTable

from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render (request, 'bandapp/home.html')


def bandlist(request):
    band = BandTable(Band.objects.all())
    RequestConfig(request).configure(band)

    band.paginate(page=request.GET.get('page', 1), per_page=10)

    return render (request, 'bandapp/bandlist.html', {'band': band})

def banddetail(request, id):
    band = Band.objects.get(id=id)
    members = MemberTable(Member.objects.all().filter(band=band))
    RequestConfig(request).configure(members)
    members.paginate(page=request.GET.get('page', 1), per_page=10)
    #band = get_object_or_404(Band, id=id)
    #members = get_object_or_404 (Member, band=band)
    # members = Member.objects.all().filter(band=band)

    context = {'members': members, 'band': band}
    return render(request,'bandapp/band_detail.html', context)

@login_required(login_url='bandapp/accounts/login/')
def protected_view(request):
    """ A view that can only be accessed by logged-in users """
    return render(request, 'bandapp/protected.html', {'current_user': request.user})

def message(request):
    """ Message if is not authenticated. Simple view! """
    return HttpResponse('Access denied!')
