from django.shortcuts import render

# Create your views here.

def home_screen_view(request):

    context = {}
    context['some_string'] = "This string was added through the context."

    return render(request, "personal/home.html", context)
