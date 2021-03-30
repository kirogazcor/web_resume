from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
import web_resume

urlpatterns = [
    path('', views.index, name='index'),
    path('education', views.education, name='education'),
    path('projects', views.projects, name='projects'),
    path('work', views.work, name='work'),
] + static(web_resume.settings.MEDIA_URL, document_root=web_resume.settings.MEDIA_ROOT)