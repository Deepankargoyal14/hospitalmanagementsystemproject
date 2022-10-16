# in this file we can create some python functions that makes a web request and returns a web response.
# this response can be a html contents of a webpage, or a redirect or a 404 erroe(not found), or an xml documents or anything else
# each view function takes http request as its first parameter.
#render is the shortcut function to return the given template.

from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')