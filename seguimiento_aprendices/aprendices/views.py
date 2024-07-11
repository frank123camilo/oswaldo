from django.shortcuts import render,get_object_or_404, redirect

from .models import Aprendices

from .forms  import AprendicesForm
 


def base(request):
   return render(request, "base.html" )

# Create your views here.
def aprendices(request):
    aprendices = Aprendices.objects.all()
    return render(request, 'aprendices.html', {'aprendices': aprendices})

def agregar(request):
    formulario= AprendicesForm(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('aprendices')
    return render(request, 'agregar.html', {'formulario': formulario})
    
def editar(request, id): 
    aprendices = get_object_or_404(Aprendices, id=id)
    
    if request.method == 'POST':
        formulario = AprendicesForm(request.POST, instance=aprendices)
        if formulario.is_valid():
            formulario.save()
            return redirect('aprendices')
    else:
        formulario= AprendicesForm(instance=aprendices)
    return render(request, 'editar.html', {'formulario': formulario})

def eliminar(reques,id):
    aprendices=get_object_or_404(Aprendices,id=id)
    aprendices.delete()
    return redirect('aprendices')
