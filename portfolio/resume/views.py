from django.shortcuts import render
from .models import Project, Skill, Achievement

def home(request):
    """Render the home page with portfolio content including projects, 
    skills, and achievements ordered by relevance."""
    #try:
    context = {
        'projects': Project.objects.all().order_by('-id'),
        'skills': Skill.objects.all().order_by( '-proficiency'),
        'achievements': Achievement.objects.all().order_by('-date')
        }
    return render(request, 'resume/home.html', context)
    # except Exception as e:
    #     # Consider adding proper error handling/logging here
    #     return render(request, 'resume/error.html', status=500)