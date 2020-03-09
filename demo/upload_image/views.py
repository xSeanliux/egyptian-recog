from django.shortcuts import render
from .models import Img
from django.http import HttpResponse
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt 
@csrf_exempt


# Create your views here.

def index(request):
    template = get_template('index.html')
    html = template.render()
    return HttpResponse(html)

def work(request):
    if request.method == "POST":
        img_name = "new_image"
        img_con = request.FILES.get('image_content')
        img = Img(img_name=img_name, img_con=img_con)
        img.save()
    template = get_template('work-single.html')
    html = template.render()
    return HttpResponse(html)

def about(request):
    template = get_template('about.html')
    html = template.render()
    return HttpResponse(html)

def contact(request):
    template = get_template('contact.html')
    html = template.render()
    return HttpResponse(html)