from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
data={
    "blogs":[
        {
            "id": 1,
            "title": "Komple Web Geliştirme",
            "image": "1.png",
            "is_active": True,
            "is_home": True,
            "description": "Çok iyi bir kurs"
        },
        {
            "id": 2,
            "title": "Python",
            "image": "2.png",
            "is_active": False,
            "is_home": True,
            "description": "PythonPython"
        },
        {
            "id": 3,
            "title": "Mobil Uygulama",
            "image": "3.png",
            "is_active": True,
            "is_home": False,
            "description": "MobilMobil"
        },
    ]
}


def index(request):
    context={
        "blogs":data["blogs"]
    }
    return render(request, "blog/index.html",context)

def blogs(request):
    context={
        "blogs":data["blogs"]
    }
    return render(request, "blog/blogs.html",context)