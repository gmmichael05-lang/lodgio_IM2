from django.shortcuts import render
from .models import SearchLog

def search_list(request):
    searches = SearchLog.objects.all()
    return render(request, 'search/search_list.html', {'searches': searches})