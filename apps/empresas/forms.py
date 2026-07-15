# apps/empresas/forms.py
from django import forms
from .models import Empresa


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
        cnpj = self.cleaned_data['cnpj']
        cnpj_limpo = ''.join(filter(str.isdigit, cnpj))
        if len(cnpj_limpo) != 14:
            raise forms.ValidationError('CNPJ deve conter 14 dígitos.')
        return cnpj_limpo