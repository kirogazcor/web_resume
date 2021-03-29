from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import AboutMe, Education, Projects

Now = datetime.datetime.now()
Year = str(Now.year)

def index(request):
    about_me_db = AboutMe.objects.all().first()
    main_content = {
        'title': 'Резюме',
        'Year': Year,
        'about_me_db': about_me_db,
    }
    return render(request, 'homePage.html', main_content)

def education(request):
    education_db = Education.objects.all()
    education_content = {
        'title': 'Образование',
        'Now': Now,
        'Year': Year,
        'education_db': education_db,
    }
    return render(request, 'education.html', education_content)

def projects(request):
    projects_db = Projects.objects.all()
    projects_content = {
        'title': 'Проекты',
        'Year': Year,
        'projects_db': projects_db,
    }
    return render(request, 'projects.html', projects_content)
# Create your views here.
