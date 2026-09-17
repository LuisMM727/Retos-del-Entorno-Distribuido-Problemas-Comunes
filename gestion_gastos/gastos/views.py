from django.shortcuts import render, redirect
from .models import Gasto

def registrar_gasto(request):
    if request.method == 'POST':
        monto = request.POST.get('monto')
        categoria = request.POST.get('categoria')
        descripcion = request.POST.get('descripcion')
        fecha = request.POST.get('fecha')

        if monto and float(monto) > 0 and categoria:
            Gasto.objects.create(
                monto=monto,
                categoria=categoria,
                descripcion=descripcion,
                fecha=fecha
            )
            return redirect('lista_gastos')

    return render(request, 'gastos/registrar.html')

def lista_gastos(request):
    gastos = Gasto.objects.all().order_by('-fecha')
    return render(request, 'gastos/lista.html', {'gastos': gastos})