#-*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.forms import BaseFormSet

from apps.default.forms import UserRegisterForm
from apps.subclasses.empresa.escola.models import Escola
from apps.default.models import Documento


class RequiredFormSet(BaseFormSet):
	def __init__(self, *args, **kwargs):
		super(RequiredFormSet, self).__init__(*args, **kwargs)
		for form in self.forms:
			form.empty_permitted = False

class PassageiroRegisterForm(UserRegisterForm, forms.ModelForm):

	id_escola = forms.ModelChoiceField (label='Escola:', queryset = Escola.objects.all(), required=False)
	matricula = forms.IntegerField(label='Matricula CN:')
	natularidade = forms.CharField(label='Natularidade:', max_length=30)
	observacao = forms.CharField(label='Obs:', max_length=250, widget=forms.Textarea)
	numero_passaporte = forms.CharField(label='Numero do Passaporte:', max_length=10, required=False)
	data_validade_passaporte = forms.DateField(required=False)

	nome_pai = forms.CharField(label='Nome do pai:', max_length=500, required=False)
	nome_mae = forms.CharField(label='Nome da mãe:', max_length=500, required=False)
	responsavel = forms.CharField(label='Nome responsável:', max_length=500, required=False)
	telefone_responsavel = forms.CharField(label='Telefone responsável:', max_length=12, required=False)
	email_responsavel = forms.EmailField(label='Email responsável:', required=False)


	def __init__(self, *args, **kwargs):
		super(PassageiroRegisterForm, self).__init__(*args, **kwargs)
		self.fields['password'].required = False
		self.fields['repetir_password'].required = False
		self.fields['id_escola'].widget.attrs['class'] = 'form-control'
		self.fields['id_escola'].required = False
		self.fields['matricula'].widget.attrs['class'] = 'form-control'
		self.fields['matricula'].widget.attrs['placeholder'] = 'Digite a matricula'
		self.fields['matricula'].required = False
		self.fields['natularidade'].widget.attrs['class'] = 'form-control'
		self.fields['natularidade'].widget.attrs['placeholder'] = 'Digite a natularidade'
		self.fields['natularidade'].required = False
		self.fields['observacao'].widget.attrs['class'] = 'form-control'
		self.fields['observacao'].widget.attrs['placeholder'] = 'Digite algumas observacões'
		self.fields['observacao'].required = False
		self.fields['numero_passaporte'].widget.attrs['class'] = 'form-control'
		self.fields['data_validade_passaporte'].widget.attrs['class'] = 'form-control'

		self.fields['nome_pai'].widget.attrs['class'] = 'form-control'
		self.fields['nome_pai'].widget.attrs['placeholder'] = 'Digite o nome do pai'
		self.fields['nome_mae'].widget.attrs['class'] = 'form-control'
		self.fields['nome_mae'].widget.attrs['placeholder'] = 'Digite o nome da mãe'
		self.fields['responsavel'].widget.attrs['class'] = 'form-control'
		self.fields['responsavel'].widget.attrs['placeholder'] = 'Digite o nome do responsável'
		self.fields['telefone_responsavel'].widget.attrs['class'] = 'form-control'
		self.fields['telefone_responsavel'].widget.attrs['placeholder'] = 'Digite o telefone do responsável'
		self.fields['email_responsavel'].widget.attrs['class'] = 'form-control'
		self.fields['email_responsavel'].widget.attrs['placeholder'] = 'Digite o email do responsável'

class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento
        fields = ('id_tipo_documento', 'anexo',)

    def __init__(self, *args, **kwargs):
        super(DocumentoForm, self).__init__(*args, **kwargs)
        self.fields['id_tipo_documento'].widget.attrs['class'] = 'form-control'
        self.fields['id_tipo_documento'].widget.attrs['placeholder'] = 'Tipo'
        self.fields['id_tipo_documento'].required = False
        self.fields['anexo'].widget.attrs['class'] = 'form-control'
        self.fields['anexo'].widget.attrs['placeholder'] = 'Anexo'
        self.fields['anexo'].required = False

        self.fields['id_tipo_documento'].label = 'Tipo de Documento'