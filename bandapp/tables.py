import django_tables2 as tables
from .models import Band, Member
from django_tables2.utils import A

class BandTable(tables.Table):
    # name = tables.LinkColumn('bandapp:banddetail', args=[A('id')])
    name = tables.LinkColumn('bandapp:banddetail', args=[A('id')])
    class Meta:
        model = Band
        fields = ('name', 'can_rock')
        attrs = {"class": "table table-striped table-bordered table-hover .table-responsive-md"}
        template = 'django_tables2/bootstrap.html'

class MemberTable(tables.Table):
    class Meta:
        model = Member
        fields = ('name', 'instrument')
        attrs = {"class": "table table-striped table-bordered table-hover"}
        # template = 'django_tables2/bootstrap.html'
        template = 'django_tables2/bootstrap.html'
