from django.shortcuts import render
from core.models import Portfolio, PortfolioFile
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    portfolios = Portfolio.objects.all()

    pagination = Paginator(portfolios, per_page=4)
    page = pagination.get_page(request.GET.get("page"))
    page_count = pagination.num_pages

    data = {
        "portfolio_page":page,
        "page_count":page_count,
        "page_count_iterator":[i for i in range(1, page_count+1)],
    }

    return render(request, "home.html", data)

def project(request, uuid):
    portfolio = Portfolio.objects.get(id=uuid)

    data = {
        "project":portfolio,
    }

    return render(request, "project.html", data)