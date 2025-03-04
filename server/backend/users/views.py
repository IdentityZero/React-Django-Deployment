from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import JsonResponse


# Create your views here.
def fetch_users(request):
    queryset = User.objects.all().values()
    return JsonResponse(list(queryset), safe=False)
