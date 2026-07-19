# apps/usuarios/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from .forms import LoginForm, UsuarioCriarForm
from .services import usuario_autenticar, usuario_criar
from .selectors import usuario_listar_por_empresa, usuario_obter_por_email


@require_http_methods(["GET", "POST"])
def login_view(request):
    """View de login."""
    if request.user.is_authenticated:
        return redirect('usuarios:dashboard')
    
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = usuario_autenticar(email, password)
            
            if user:
                login(request, user)
                user.atualizar_ultimo_acesso()
                messages.success(request, f'Bem-vindo, {user.get_short_name()}!')
                return redirect('usuarios:dashboard')
            else:
                messages.error(request, 'E-mail ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = LoginForm()
    
    return render(request, 'usuarios/login.html', {'form': form})


@require_http_methods(["POST"])
def logout_view(request):
    """View de logout."""
    logout(request)
    messages.info(request, 'Você saiu do sistema.')
    return redirect('usuarios:login')


@login_required
def dashboard_view(request):
    """Dashboard principal."""
    empresa = getattr(request.user, 'empresa', None)
    return render(request, 'usuarios/dashboard.html', {
        'usuario': request.user,
        'empresa': empresa,
    })