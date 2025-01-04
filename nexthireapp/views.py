from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')
def blog_details(request):
    return render(request,'blog-details.html')

def events(request):
    return render(request,'events.html')

def service(request):
    return render(request,'service.html')

def about(request):
    return render(request,'about-us.html')

def vision(request):
    return render(request,'vision.html')

def mission(request):
    return render(request,'mission.html')