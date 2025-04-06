from django.shortcuts import render
from .models import LatestNews
from django.http import HttpResponse

context = {
    'latest_news': LatestNews.objects.filter(is_active=True).order_by('-date')[:5],
}

# Create your views here.
def home(request):
    return render(request, 'home.html', context)