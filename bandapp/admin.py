from django.contrib import admin

# Register your models here.
'''
# python manage.py loaddata fixtures.json
import band information into model.

'''
from .models import Band, Member

class MemberAdmin(admin.ModelAdmin):

    """Customize the look of the auto-generated admin for the Member model"""
    list_display = ('name', 'instrument')
    list_filter = ('band',)

admin.site.register(Band)  # Use the default options
admin.site.register(Member, MemberAdmin)  # Use the customized options
