# apps/empresas/forms.py
from django import forms
from .models import Empresa
from django.core.exceptions import ValidationError as DjangoVE
from apps.core.utils import limpar_cnpj

class EmpresaForm(forms.ModelForm):
    """Formulário de criação/edição de empresa."""
    
    class Meta:
        model = Empresa
        fields = [
            'nome', 'nome_fantasia', 'cnpj', 'inscricao_estadual',
            'inscricao_municipal', 'telefone', 'celular', 'email', 'site',
            'cep', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'estado',
            'logo', 'cor_primaria', 'cor_secundaria',
            'modulo_vendas', 'modulo_compras', 'modulo_estoque', 'modulo_financeiro',
        ]
        widgets = {
            'cor_primaria': forms.TextInput(attrs={'type': 'color'}),
            'cor_secundaria': forms.TextInput(attrs={'type': 'color'}),
        }
    
    def clean_cnpj(self):
        try:
            return limpar_cnpj(self.cleaned_data['cnpj'])
        except ValueError as e:
            raise forms.ValidationError(str(e))