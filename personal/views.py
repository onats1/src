from django.shortcuts import render


# Create your views here.
from account.models import Account


def home_screen_view(request):

    context = {}
    accounts = Account.objects.all()
    context['accounts'] = accounts
    context['random_number'] = "12345678889"

    return render(request, "personal/home.html", context)
