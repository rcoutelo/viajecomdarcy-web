#-*- coding: utf-8 -*-


##################################################
#               DJANGO IMPORTS                   #
##################################################
from django import forms
##################################################


##################################################
#               CUSTOM IMPORTS                   #
##################################################
from .models import Reserva, ReservaPassageiro, PassageiroOpcional
from apps.excursao.models import Excursao, Opcional
from apps.pacote.models import Pacote
from apps.subclasses.usuario.passageiro.models import Passageiro
from apps.acomodacao.models import Acomodacao
from apps.moeda.models import Moeda
##################################################


class FiltroReservaForm(forms.Form):

    data_inicio = forms.DateField()
    data_fim = forms.DateField()

    def __init__(self, *args, **kwargs):
        super(FiltroReservaForm, self).__init__(*args, **kwargs)

        self.fields['data_inicio'].widget.attrs['class'] = 'form-control'
        self.fields['data_fim'].widget.attrs['class'] = 'form-control'
        self.fields['data_inicio'].widget.attrs['placeholder'] = 'Data de inicio'
        self.fields['data_fim'].widget.attrs['placeholder'] = 'Data de término'


class ReservaForm(forms.ModelForm):

    class Meta:
        model = Reserva
        fields = ('id_cliente','id_status_reserva')


    def __init__(self, *args, **kwargs):
        super(ReservaForm, self).__init__(*args, **kwargs)
        # id_cliente Fields widget
        self.fields['id_cliente'].widget.attrs['class'] = 'form-control'
        # id_status_reserva  Fields widget
        self.fields['id_status_reserva'].widget.attrs['class'] = 'form-control'

    pass


class NovaReservaForm(forms.ModelForm):

    id_passageiro = forms.ModelChoiceField(queryset=Passageiro.objects.all())

    class Meta:
        model = Reserva
        fields = ['id_cliente']


    def __init__(self, *args, **kwargs):
        super(NovaReservaForm, self).__init__(*args, **kwargs)
        self.fields['id_cliente'].widget.attrs['class'] = 'form-control'
        self.fields['id_passageiro'].widget.attrs['class'] = 'form-control'


class NovaReservaPassageiroForm(forms.ModelForm):

    id_excursao = forms.ModelChoiceField (queryset=Excursao.objects.all())

    class Meta:
        model = ReservaPassageiro
        exclude = ['id_reserva','id_passageiro','id_status_reserva_passageiro','id_escola', 'passageiro_opcional']


    def __init__(self, *args, **kwargs):
        super(NovaReservaPassageiroForm, self).__init__(*args, **kwargs)
        # id_reserva Fields widget
        self.fields['id_excursao'].widget.attrs['class'] = 'form-control form-excursao'
        self.fields['id_excursao'].required = True
        self.fields['id_excursao'].widget.attrs['onchange'] = 'setExcursaoPacote(this)'

        # id_pacote Fields widget
        self.fields['id_pacote'].widget.attrs['class'] = 'form-control form-pacote'
        self.fields['id_pacote'].required = True
        self.fields['id_pacote'].widget.attrs['onchange'] = 'setPacoteAcomodacao(this)'

        # reserva_passageiro_preco Fields widget
        self.fields['reserva_passageiro_preco'].widget.attrs['class'] = 'form-control'
        self.fields['reserva_passageiro_preco'].required = True

        # reserva_passageiro_cambio  Fields widget
        self.fields['id_moeda'].widget.attrs['class'] = 'form-control form-moeda'
        self.fields['id_moeda'].required = False

        # reserva_passageiro_cambio  Fields widget
        self.fields['reserva_passageiro_cambio'].widget.attrs['class'] = 'form-control'
        self.fields['reserva_passageiro_cambio'].required = True

        # reserva_passageiro_obs  Fields widget
        self.fields['reserva_passageiro_obs'].widget.attrs['class'] = 'form-control'
        self.fields['reserva_passageiro_obs'].required = False

        # registro_interno  Fields widget
        self.fields['registro_interno'].widget.attrs['class'] = 'form-control'
        self.fields['registro_interno'].required = False

        # desconto  Fields widget
        self.fields['desconto'].widget.attrs['class'] = 'form-control'
        self.fields['desconto'].required = True

        # id_acomodacao_pacote  Fields widget
        self.fields['id_acomodacao_pacote'].widget.attrs['class'] = 'form-control form-acomodacao'
        self.fields['id_acomodacao_pacote'].widget.attrs['onchange'] = 'setPrecoAcomodacao(this)'
        self.fields['id_acomodacao_pacote'].required = True

        # preco_acomodacao  Fields widget
        self.fields['preco_acomodacao'].widget.attrs['class'] = 'form-control form-preco'
        self.fields['preco_acomodacao'].required = True
        pass

class ReservaPassageiroForm(forms.ModelForm):

    id_excursao = forms.ModelChoiceField (queryset=Excursao.objects.all())
    id_pacote = forms.ModelChoiceField (queryset=Pacote.objects.all())
    id_acomodacao_pacote = forms.ModelChoiceField (queryset=Acomodacao.objects.all())
    id_moeda = forms.ModelChoiceField (queryset=Moeda.objects.all(), required=False)
    reserva_passageiro_obs = forms.CharField(required=False)
    registro_interno = forms.CharField(required=False)
    desconto = forms.DecimalField(required=False)

    class Meta:
        model = ReservaPassageiro
        fields = (
            'id_status_reserva_passageiro',
            'reserva_passageiro_preco','reserva_passageiro_cambio', 
            'preco_acomodacao'
            )


    def __init__(self, *args, **kwargs):
        super(ReservaPassageiroForm, self).__init__(*args, **kwargs)
        # id_reserva Fields widget
        self.fields['id_excursao'].widget.attrs['class'] = 'form-control form-excursao'
        self.fields['id_excursao'].widget.attrs['onchange'] = 'setExcursaoPacote(this)'
        # id_pacote Fields widget
        self.fields['id_pacote'].widget.attrs['class'] = 'form-control form-pacote'
        self.fields['id_pacote'].widget.attrs['onchange'] = 'setPacoteAcomodacao(this)'
        # id_status_reserva_passageiro  Fields widget
        self.fields['id_status_reserva_passageiro'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_preco Fields widget
        self.fields['reserva_passageiro_preco'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_cambio  Fields widget
        self.fields['id_moeda'].widget.attrs['class'] = 'form-control form-moeda'
        # reserva_passageiro_cambio  Fields widget
        self.fields['reserva_passageiro_cambio'].widget.attrs['class'] = 'form-control'
        # reserva_passageiro_obs  Fields widget
        self.fields['reserva_passageiro_obs'].widget.attrs['class'] = 'form-control'
        # registro_interno  Fields widget
        self.fields['registro_interno'].widget.attrs['class'] = 'form-control'
        # desconto  Fields widget
        self.fields['desconto'].widget.attrs['class'] = 'form-control'
        # id_acomodacao_pacote  Fields widget
        self.fields['id_acomodacao_pacote'].widget.attrs['class'] = 'form-control form-acomodacao'
        self.fields['id_acomodacao_pacote'].widget.attrs['onchange'] = 'setPrecoAcomodacao(this)'
        # preco_acomodacao  Fields widget
        self.fields['preco_acomodacao'].widget.attrs['class'] = 'form-control form-preco'
    pass

class ReservaOpcionaisForm(forms.ModelForm):

    id_passageiro = forms.ModelChoiceField (queryset=Passageiro.objects.all())
    id_moeda = forms.ModelChoiceField (queryset=Moeda.objects.all(), required=False)
    moeda_desc = forms.CharField(required=False)

    class Meta:
        model = PassageiroOpcional
        fields = (
            'id_reserva_passageiro',
            'id_opcional',
            'preco_reserva_opcional'
            )


    def __init__(self, *args, **kwargs):
        #self.id_passageiros = kwargs.pop('id_passageiros')
        super(ReservaOpcionaisForm, self).__init__(*args, **kwargs)
        # id_reserva_passageiro Fields widget
        self.fields['id_reserva_passageiro'].widget.attrs['class'] = 'form-control'
        # id_opcional Fields widget
        self.fields['id_opcional'].widget.attrs['class'] = 'form-control form-opcional'
        self.fields['id_opcional'].widget.attrs['onchange'] = 'setPassageiroMoedaOpcional(this)'
        # preco_reserva_opcional Fields widget
        self.fields['preco_reserva_opcional'].widget.attrs['class'] = 'form-control'
        # id_passageiro Fields widget
        self.fields['id_passageiro'].widget.attrs['class'] = 'form-control'
        #self.fields['id_passageiro'].queryset = Passageiro.objects.filter(pk__in=self.id_passageiros)
        self.fields['id_passageiro'].widget.attrs['onchange'] = 'setPassageiroOpcional(this)'
        # id_moeda  Fields widget
        self.fields['id_moeda'].widget.attrs['class'] = 'form-control'
        self.fields['moeda_desc'].widget.attrs['class'] = 'form-control form-moeda'
    pass