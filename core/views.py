from django.shortcuts import render
from core.models import Portfolio, PortfolioFile

# Create your views here.
def home(request):
    portfolios = Portfolio.objects.all()

    data = {
        "portfolios":portfolios,
    }

    return render(request, "home.html", data)

def project(request, uuid):
    portfolio = Portfolio.objects.get(id=uuid)

    data = {
        "project":portfolio,
    }

    return render(request, "project.html", data)