from django.forms import ModelForm
from .models import Project

#El formulario que voy a crear estará basado en la clase Project que tiene todas las caracteristicas de un projecto
class ProjectForm(ModelForm):
      class Meta:
          model = Project  #Del modelo (tabla) haz otro modelo para el formulario pero con los siguiente archivos
          fields = ['title','featured_image', 'description','demo_link', 'source_link', 'tags']
