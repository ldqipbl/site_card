from django.shortcuts import render
from .models import portfolio_project
from .models import career_path


# Create your views here.

def main(request):
    return render(request, 'mainapp/index.html')

def about_me(request):
    return render(request, 'mainapp/about_me.html')

def career(request):
    career_paths = career_path.objects.all()
    content = {'career_paths': career_paths}
    return render(request, 'mainapp/career.html', content)

def portfolio(request):
    portfolio_projects = portfolio_project.objects.all()
    content = {'portfolio_projects': portfolio_projects}
    return render(request, 'mainapp/portfolio.html', content)

def resume(request):
    return render(request, 'mainapp/resume.txt')
