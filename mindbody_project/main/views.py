from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def blog(request):
    return render(request, 'main/blog.html')

def gallery(request):
    return render(request, 'main/gallery.html')
