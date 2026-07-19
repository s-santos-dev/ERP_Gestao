#!/usr/bin/env python
"""
Carga de Empresas Ficticias - ERP Gestao
==========================================
Script standalone. Roda com UM comando no terminal.

USO:
    python scripts/empresas_seed.py

Ou com quantidade customizada:
    python scripts/empresas_seed.py 20
"""

import os
import sys
import random
from datetime import date, timedelta

# === SETUP DJANGO ===
# Detecta automaticamente o diretorio do projeto e adiciona ao PYTHONPATH
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)  # scripts/ -> ERP_Gestao/

# ADICIONA o projeto ao PYTHONPATH para o Django encontrar os modulos
sys.path.insert(0, project_dir)
os.chdir(project_dir)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

import django
django.setup()

from django.contrib.auth import get_user_model
from apps.empresas.models import Empresa

Usuario = get_user_model()


# =============================================================================
# DADOS FICTICIOS
# =============================================================================

NOMES_EMPRESAS = [
    ('TechSolucoes Inteligentes Ltda', 'TechSol'),
    ('Mega Distribuidora Nacional S.A.', 'MegaDist'),
    ('Construtora Horizonte Verde Ltda', 'Horizonte'),
    ('Supermercados Bom Preco S.A.', 'BomPreco'),
    ('Auto Pecas Veloz Ltda', 'VelozPecas'),
    ('Farmacia Saude Total S.A.', 'SaudeTotal'),
    ('Moveis Planejados Artesanal Ltda', 'ArtMoveis'),
    ('Transportadora RodoNorte S.A.', 'RodoNorte'),
    ('Consultoria Estrategica Alpha Ltda', 'AlphaConsult'),
    ('Industria Textil Brasil S.A.', 'TextilBR'),
    ('Panificadora Pao de Ouro Ltda', 'PaoOuro'),
    ('Academia Fitness Pro S.A.', 'FitnessPro'),
    ('Loja de Eletronicos FutureTech Ltda', 'FutureTech'),
    ('Restaurante Sabores do Brasil Ltda', 'SaboresBR'),
    ('Imobiliaria Casa Nova S.A.', 'CasaNova'),
    ('Escola de Idiomas Global Speak Ltda', 'GlobalSpeak'),
    ('Pet Shop Amigo Fiel S.A.', 'AmigoFiel'),
    ('Lavanderia Express Clean Ltda', 'ExpressClean'),
    ('Oficina Mecanica Turbo Max S.A.', 'TurboMax'),
    ('Clinica Odontologica Sorriso Perfeito Ltda', 'SorrisoPerfeito'),
]

CNPJS_FICTICIOS = [
    '11.222.333/0001-44', '22.333.444/0001-55', '33.444.555/0001-66',
    '44.555.666/0001-77', '55.666.777/0001-88', '66.777.888/0001-99',
    '77.888.999/0001-00', '88.999.000/0001-11', '99.000.111/0001-22',
    '00.111.222/0001-33', '12.345.678/0001-90', '98.765.432/0001-10',
    '45.678.901/0001-23', '67.890.123/0001-45', '89.012.345/0001-67',
    '01.234.567/0001-89', '23.456.789/0001-01', '34.567.890/0001-12',
    '56.789.012/0001-34', '78.901.234/0001-56',
]

ENDERECOS = [
    {'cep': '01310-100', 'logradouro': 'Av. Paulista', 'numero': '1000', 'bairro': 'Bela Vista', 'cidade': 'Sao Paulo', 'estado': 'SP'},
    {'cep': '20040-010', 'logradouro': 'Rua do Ouvidor', 'numero': '150', 'bairro': 'Centro', 'cidade': 'Rio de Janeiro', 'estado': 'RJ'},
    {'cep': '30140-071', 'logradouro': 'Av. Afonso Pena', 'numero': '800', 'bairro': 'Centro', 'cidade': 'Belo Horizonte', 'estado': 'MG'},
    {'cep': '40020-000', 'logradouro': 'Av. Sete de Setembro', 'numero': '2000', 'bairro': 'Comercio', 'cidade': 'Salvador', 'estado': 'BA'},
    {'cep': '80010-000', 'logradouro': 'Rua XV de Novembro', 'numero': '500', 'bairro': 'Centro', 'cidade': 'Curitiba', 'estado': 'PR'},
    {'cep': '90010-150', 'logradouro': 'Av. Borges de Medeiros', 'numero': '2500', 'bairro': 'Praia de Belas', 'cidade': 'Porto Alegre', 'estado': 'RS'},
    {'cep': '51020-000', 'logradouro': 'Av. Boa Viagem', 'numero': '3000', 'bairro': 'Boa Viagem', 'cidade': 'Recife', 'estado': 'PE'},
    {'cep': '74003-010', 'logradouro': 'Av. Goias', 'numero': '1000', 'bairro': 'Setor Central', 'cidade': 'Goiania', 'estado': 'GO'},
    {'cep': '69005-000', 'logradouro': 'Av. Eduardo Ribeiro', 'numero': '700', 'bairro': 'Centro', 'cidade': 'Manaus', 'estado': 'AM'},
    {'cep': '64001-000', 'logradouro': 'Av. Frei Serafim', 'numero': '1200', 'bairro': 'Centro', 'cidade': 'Teresina', 'estado': 'PI'},
]

CORES_PRIMARIAS = ['#0d6efd', '#6610f2', '#6f42c1', '#d63384', '#dc3545', '#fd7e14', '#ffc107', '#198754', '#20c997', '#0dcaf0', '#adb5bd', '#212529']
CORES_SECUNDARIAS = ['#6c757d', '#adb5bd', '#dee2e6', '#e9ecef', '#f8f9fa', '#495057', '#343a40', '#212529']

TELEFONES = ['(11) 3000-0001', '(21) 3000-0002', '(31) 3000-0003', '(71) 3000-0004', '(41) 3000-0005', '(51) 3000-0006', '(81) 3000-0007', '(62) 3000-0008', '(92) 3000-0009', '(86) 3000-0010', '(11) 4000-0001', '(21) 4000-0002']
CELULARES = ['(11) 98765-4321', '(21) 98765-4322', '(31) 98765-4323', '(71) 98765-4324', '(41) 98765-4325', '(51) 98765-4326', '(81) 98765-4327', '(62) 98765-4328', '(92) 98765-4329', '(86) 98765-4330', '(11) 91234-5678', '(21) 91234-5679']
EMAILS = ['contato@techsol.com.br', 'sac@megadist.com.br', 'obra@horizonte.com.br', 'atendimento@bompreco.com.br', 'pecas@velozpecas.com.br', 'farmacia@saudetotal.com.br', 'vendas@artmoveis.com.br', 'logistica@rodonorte.com.br', 'consultoria@alpha.com.br', 'vendas@textilbr.com.br', 'padaria@paodeouro.com.br', 'matricula@fitnesspro.com.br', 'suporte@futuretech.com.br', 'reservas@saboresbr.com.br', 'imoveis@casanova.com.br', 'info@globalspeak.com.br', 'agenda@amigofiel.com.br', 'coleta@expressclean.com.br', 'agendamento@turbomax.com.br', 'consulta@sorrisoperfeito.com.br']
SITES = ['https://www.techsol.com.br', 'https://www.megadist.com.br', 'https://www.horizonte.com.br', 'https://www.bompreco.com.br', 'https://www.velozpecas.com.br', 'https://www.saudetotal.com.br', 'https://www.artmoveis.com.br', 'https://www.rodonorte.com.br', 'https://www.alphaconsult.com.br', 'https://www.textilbr.com.br', 'https://www.paodeouro.com.br', 'https://www.fitnesspro.com.br', 'https://www.futuretech.com.br', 'https://www.saboresbr.com.br', 'https://www.casanova.com.br', 'https://www.globalspeak.com.br', 'https://www.amigofiel.com.br', 'https://www.expressclean.com.br', 'https://www.turbomax.com.br', 'https://www.sorrisoperfeito.com.br']
INSCRICOES_ESTADUAIS = ['123.456.789.012', '987.654.321.098', '456.789.012.345', '789.012.345.678', '012.345.678.901', '345.678.901.234', '678.901.234.567', '901.234.567.890', '234.567.890.123', '567.890.123.456', '111.222.333.444', '555.666.777.888']
INSCRICOES_MUNICIPAIS = ['1234567', '7654321', '1122334', '5566778', '9988776', '3344556', '7788990', '0011223', '4455667', '8899001']


# =============================================================================
# FUNCOES
# =============================================================================

def limpar_cnpj(cnpj):
    return ''.join(filter(str.isdigit, cnpj))


def gerar_data_expiracao():
    dias = random.randint(365, 1095)
    return date.today() + timedelta(days=dias)


def escolher_modulos():
    return {
        'modulo_vendas': random.choice([True, True, True, False]),
        'modulo_compras': random.choice([True, True, False]),
        'modulo_estoque': random.choice([True, True, True, False]),
        'modulo_financeiro': random.choice([True, True, False]),
    }


def criar_empresas(quantidade, usuario_criador):
    empresas_criadas = []

    for i in range(quantidade):
        nome_razao, nome_fantasia = NOMES_EMPRESAS[i % len(NOMES_EMPRESAS)]
        cnpj = CNPJS_FICTICIOS[i % len(CNPJS_FICTICIOS)]
        endereco = ENDERECOS[i % len(ENDERECOS)]

        if Empresa.objects.filter(cnpj=limpar_cnpj(cnpj)).exists():
            print(f"  [PULADO] {nome_fantasia} (CNPJ ja existe)")
            continue

        empresa = Empresa.objects.create(
            nome=nome_razao,
            nome_fantasia=nome_fantasia,
            cnpj=cnpj,
            inscricao_estadual=INSCRICOES_ESTADUAIS[i % len(INSCRICOES_ESTADUAIS)],
            inscricao_municipal=INSCRICOES_MUNICIPAIS[i % len(INSCRICOES_MUNICIPAIS)],
            cor_primaria=random.choice(CORES_PRIMARIAS),
            cor_secundaria=random.choice(CORES_SECUNDARIAS),
            limite_usuarios=random.choice([3, 5, 10, 15, 20, 50]),
            data_expiracao=gerar_data_expiracao(),
            **escolher_modulos(),
            cep=endereco['cep'],
            logradouro=endereco['logradouro'],
            numero=endereco['numero'],
            bairro=endereco['bairro'],
            cidade=endereco['cidade'],
            estado=endereco['estado'],
            complemento=f"Sala {random.randint(100, 999)}" if random.random() > 0.5 else '',
            telefone=TELEFONES[i % len(TELEFONES)],
            celular=CELULARES[i % len(CELULARES)],
            email=EMAILS[i % len(EMAILS)],
            site=SITES[i % len(SITES)],
            criado_por=usuario_criador,
            atualizado_por=usuario_criador,
        )
        empresas_criadas.append(empresa)
        print(f"  [{len(empresas_criadas):02d}/{quantidade}] {empresa.nome_fantasia} - CNPJ: {empresa.cnpj}")

    return empresas_criadas


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 60)
    print("CARGA DE EMPRESAS FICTICIAS - ERP Gestao")
    print("=" * 60)

    # Parse argumento de quantidade
    quantidade = 10
    if len(sys.argv) > 1:
        try:
            quantidade = int(sys.argv[1])
        except ValueError:
            print(f"Uso: python {sys.argv[0]} [quantidade]")
            sys.exit(1)

    # Buscar usuario criador
    usuario = Usuario.objects.filter(is_superuser=True).first() or Usuario.objects.first()
    if not usuario:
        print("\nERRO: Nenhum usuario encontrado!")
        print("Crie um superuser primeiro:")
        print("  python manage.py createsuperuser")
        sys.exit(1)

    print(f"\nUsuario criador: {usuario.nome} ({usuario.email})")
    print(f"Criando {quantidade} empresas ficticias...")
    print("-" * 60)

    empresas = criar_empresas(quantidade, usuario)

    print("-" * 60)
    print(f"Empresas criadas: {len(empresas)}")
    print(f"Total no banco:   {Empresa.objects.count()}")
    print("=" * 60)
    print("OK - Carga concluida!")


if __name__ == '__main__':
    main()