# apps/empresas/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.http import JsonResponse

from .models import Empresa
from .forms import EmpresaForm
from .services import empresa_criar, empresa_atualizar, empresa_desativar
from .selectors import empresa_listar_todas, empresa_obter_por_id


@login_required
@permission_required('empresas.view_empresa', raise_exception=True)
def empresa_lista(request):
    """Lista todas as empresas."""
    empresas = empresa_listar_todas()
    return render(request, 'empresas/lista.html', {'empresas': empresas})


@login_required
@permission_required('empresas.add_empresa', raise_exception=True)
def empresa_criar_view(request):
    """View para criar nova empresa."""
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                empresa = empresa_criar(
                    nome=form.cleaned_data['nome'],
                    cnpj=form.cleaned_data['cnpj'],
                    nome_fantasia=form.cleaned_data.get('nome_fantasia', ''),
                    **{k: v for k, v in form.cleaned_data.items() 
                       if k not in ['nome', 'cnpj', 'nome_fantasia']}
                )
                messages.success(request, f'Empresa "{empresa}" criada com sucesso!')
                return redirect('empresas:lista')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = EmpresaForm()
    
    return render(request, 'empresas/form.html', {'form': form, 'titulo': 'Nova Empresa'})


@login_required
@permission_required('empresas.change_empresa', raise_exception=True)
def empresa_editar_view(request, pk):
    """View para editar empresa."""
    empresa = get_object_or_404(Empresa, pk=pk)
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST, request.FILES, instance=empresa)
        if form.is_valid():
            try:
                empresa = empresa_atualizar(empresa, **form.cleaned_data)
                messages.success(request, 'Empresa atualizada com sucesso!')
                return redirect('empresas:lista')
            except Exception as e:
                messages.error(request, str(e))
    else:
        form = EmpresaForm(instance=empresa)
    
    return render(request, 'empresas/form.html', {
        'form': form, 
        'titulo': 'Editar Empresa',
        'empresa': empresa
    })


@login_required
@permission_required('empresas.delete_empresa', raise_exception=True)
def empresa_desativar_view(request, pk):
    """Desativa uma empresa (soft-delete)."""
    empresa = get_object_or_404(Empresa, pk=pk)
    
    if request.method == 'POST':
        empresa_desativar(empresa)
        messages.success(request, 'Empresa desativada com sucesso.')
        return redirect('empresas:lista')
    
    return render(request, 'empresas/confirmar_desativar.html', {'empresa': empresa})