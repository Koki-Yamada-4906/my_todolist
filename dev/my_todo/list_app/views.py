from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import ProjectLists

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('App:home')  # 成功した場合にリダイレクトするURLを指定
        
    else:
        form = ProjectForm()

    return render(request, 'home.html', {'form': form})

def delete_view(request):
    ProjectLists.objects.all().delete()
    return redirect('App:home')

def project_lists_view(request):
    project_lists = ProjectLists.objects.order_by('-updated_at')
    return render(request, 'home.html', {'project_lists': project_lists})