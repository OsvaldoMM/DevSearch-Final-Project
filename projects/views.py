from projects.models import Project
from django.shortcuts import render, redirect
from .forms import ProjectForm

# Create your views here.

#Funcion para crear la pagina donde se presentan todos los projectos 
def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

#Funcion para crear la pagina donde se presenta cada projecto por separado
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()
    return render(request, 'projects/single-project.html', {'project': projectObj, 'tags': tags})

#Funcion para crear el formulario que a su vez va a crear un nuevo projecto
def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects') #projects lo utilizo de manera dinamica desde urls
    context = {'form': form}
    return render(request, "projects/project_form.html", context)

#Funcion para editar un projecto
def updateProject(request, pk):
    project = Project.objects.get(id=pk) #obtengo el projecto
    form = ProjectForm(instance=project) #agrego el projecto a mi formulario

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects') #projects lo utilizo de manera dinamica desde urls
    context = {'form': form}
    return render(request, "projects/project_form.html", context)
    
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)