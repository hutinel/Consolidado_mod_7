from django.shortcuts import render, redirect, get_object_or_404
from .models import Laboratorio
from .forms import LaboratorioForm
# Create your views here.

def index(request):
    return render(request, 'laboratorio/index.html')

def laboratorio_list(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/laboratorio_list.html', {'laboratorios': laboratorios})

def laboratorio_detail(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id) #El campo id nos permitira poder utilizar ese valor en la ruta de la url 
    return render(request, 'laboratorio/laboratorio_detail.html', {'laboratorio': laboratorio})

def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')
    else:
        form =LaboratorioForm()
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form, 'title': 'Ingresar datos del laboratorio' })


def laboratorio_update(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio_list')  # Redirigir a la lista de laboratorios después de actualizar
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form, 'title': 'Actualizar Laboratorio'})

    
def laboratorio_delete(request, id):
    laboratorio = get_object_or_404(Laboratorio, id=id)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio_list')
    return render(request, 'laboratorio/laboratorio_confirm_delete.html', {'laboratorio': laboratorio})
