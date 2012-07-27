# Create your views here.
#from django.utils.httpwrappers import HttpResponse
try:
    from django.http import HttpResponse, Http404
except ImportError, err:
    print err
from django.shortcuts import render, redirect, render_to_response, get_object_or_404, get_list_or_404
from gbs.cases.models import TestCase

GBS_HTML = '/home/test/workspace/gbs-test/cases/v0.9.html'

def index(request):
    return HttpResponse(open(GBS_HTML))
    #return redirect('https://otctools.jf.intel.com/pm/versions/4')

def detail(request, case_id='2'):
    return HttpResponse("You're looking at case %s." % case_id)
def detail2(request, case_id=1):
    #raise Http404
    #cases = TestCase.objects.all()
    cases = get_list_or_404(TestCase, id=case_id)
    #output ='<br/>'.join([item.summary for item in cases_list])
    return render_to_response('cases/index.html', {'cases_list': cases})
    #return HttpResponse(output)
    #return redirect('https://otctools.jf.intel.com/pm/versions/4')
