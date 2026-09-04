from django.shortcuts import render
from core.models import Portfolio, PortfolioFile, VisitorInfo, ProjectVisitInfo
from django.core.paginator import Paginator
from core.visitor_tracking import site_visits, project_visits

# Create your views here.
def home(request):
    # Track and Store visitors
    site_visits(request)

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

    project_visits(request, portfolio)     # Project visit track
    visit_count = ProjectVisitInfo.objects.filter(project=portfolio).count()     # Project visits

    data = {
        "project":portfolio,
        "visits":visit_count,
        "percent_of_total_visit":round(visit_count / VisitorInfo.objects.all().count(), 2)*100
    }

    return render(request, "project.html", data)

def about(request):
    visit_count = VisitorInfo.objects.all().count()
    data = {
        "visitor_count":visit_count
    }

    return render(request, "about.html", data)