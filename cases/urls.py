from django.conf.urls.defaults import *

urlpatterns = patterns('gbs.cases.views',
                        (r'^$', 'index'),
                        #(r'^1$', 'detail'))
                        (r'^(?P<case_id>\d+>)/$', 'detail2')
                        )
from cases.models import TestCase
info_dict = {
'queryset':TestCase.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
                        (r'^$', 'object_list', info_dict),
                        #(r'^1$', 'detail'))
                        (r'^(?P<object_id>\d+>)/$', 'object_detail', info_dict)
                        )
