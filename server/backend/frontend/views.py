from django.shortcuts import render


# Create your views here.
def main(request, path):
    return render(request, template_name="frontend/index.html")
