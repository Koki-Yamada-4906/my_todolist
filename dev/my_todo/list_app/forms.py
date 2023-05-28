from django import forms
from .models import ProjectLists

class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectLists
        fields = ['name']
