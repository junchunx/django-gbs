from django.contrib import admin
from cases.models import TestCase

class TestCaseAdmin(admin.ModelAdmin):
    list_dispaly = ['issue', 'version', 'summary']
    search_fields = ['issue']

admin.site.register(TestCase)
#admin.site.register(TestCase, TestCaseAdmin)

