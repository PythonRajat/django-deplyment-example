from django.shortcuts import render

# Create your views here.
def index(request):
    content_dict = {'text':"Hello Rajat",'Number':1234}
    return render(request,'basic_app/index.html',content_dict)

def other(request):
    return render(request,'basic_app/other.html')

def base(request):
    return render(request, 'basic_app/base.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')