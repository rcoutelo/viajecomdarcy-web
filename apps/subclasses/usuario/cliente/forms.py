#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from apps.default.forms import UserRegisterForm
##################################################

class ClienteRegisterForm(UserRegisterForm, forms.Form):

	dt_emissao_rg = forms.DateField(label='Data emissão RG:',input_formats=settings.DATE_INPUT_FORMATS)
	tempo_residencia = forms.CharField(label='Tempo de residência:', max_length=45)
	empresa = forms.CharField(label='Nome da Empresa:', max_length=45)
	cep_empresa = forms.CharField(label='Cep da empresa:', max_length=45)
	endereco_empresa = forms.CharField(label='Endereço da Empresa:', max_length=45)
	telefone_empresa = forms.CharField(label='Telefone da Empresa:', max_length=45)
	dt_admissao = forms.DateField(label='Data de adminissão:',input_formats=settings.DATE_INPUT_FORMATS)
	cargo = forms.CharField(label='Cargo ou Função:', max_length=45)
	principal_renda = forms.CharField(label='Renda Principal:', max_length=45)
	outra_renda = forms.CharField(label='Outras Rendas:', max_length=45)
	patrimonio = forms.CharField(label='Patrimonio:', max_length=45)
	banco = forms.CharField(label='Banco onde tem conta:', max_length=45)
	agencia = forms.CharField(label='Agência:', max_length=45)
	conta = forms.CharField(label='Conta:', max_length=45)
	dt_banco = forms.DateField(label='Cliente do bancos desde:',input_formats=settings.DATE_INPUT_FORMATS)
	telefone_banco = forms.CharField(label='Telefone do banco:', max_length=45)

