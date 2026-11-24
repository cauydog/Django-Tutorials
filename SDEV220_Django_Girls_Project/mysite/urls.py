from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Django Girls Blog Project</h1><p>Project is running. Open <a href="/admin/">Django admin</a> to manage blog posts.</p>')


urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
]
