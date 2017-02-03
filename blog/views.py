from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    # context = locals()
    context = {'year':datetime.datetime.now().year}
    template = "home.html"
    return render(request, template, context)
