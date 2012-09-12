# Create your views here.
#from django.template import Context, loader
from django.http import HttpResponse
from django.shortcuts import render_to_response

#from django.conf import settings
import os
import StringIO
import sys
def index(request):

    saveout = sys.stdout
    log_out = StringIO.StringIO()  
    sys.stdout = log_out 

    from django.core.management import execute_from_command_line

    execute_from_command_line(["manage.py", "syncdb", "--noinput"])
    
    result = log_out.getvalue()
    sys.stdout = saveout
    return HttpResponse(result.replace("\n","<br/>"))
    
