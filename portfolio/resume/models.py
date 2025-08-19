
# Create your models here.
from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=50)
    proficiency = models.IntegerField(
        default=3,
        choices=[(1, 'Basic'), (2, 'Novice'), (3, 'Intermediate'), (4, 'Advanced'), (5, 'Expert')]
    )

    def __str__(self):
        return f"{self.name} ({self.get_proficiency_display()})"

class Project(models.Model):
    PROJECT_TYPES = [
        ('JAVA', 'Java'),
        ('PYTHON', 'Python'),
        ('INTERNSHIP', 'Internship Project'),
        ('DJANGO', 'Django')
    ]
    
    title = models.CharField(max_length=100)
    resume_description = models.TextField()  # Copy from your resume
    extended_description = models.TextField(blank=True)  # For future details
    github_url = models.URLField()
    skills = models.ManyToManyField(Skill)
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    issuer = models.CharField(max_length=100)
    verify_url = models.URLField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.issuer}"