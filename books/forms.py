from django import forms
from django.forms.models import inlineformset_factory
from books.models import Nf, Oppkg, Subscriber

class NfForm(forms.ModelForm):
    class Meta:
        model = Nf
        fields = ['name']


class OppkgForm(forms.ModelForm):
    class Meta:
        model = Oppkg
        fields = ['operator','sw_pkg','nfs', 'sess_5gm', 'comment']

        widgets = {
             'operator': forms.Select(attrs={'class': 'form-select form-select-sm'}),
             'sw_pkg': forms.Select(attrs={'class': 'form-select form-select-sm'}),
             'nfs': forms.CheckboxSelectMultiple(),
             'sess_5gm': forms.NumberInput(attrs={'class': 'form-control'}),
             'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
        labels = {
            'operator': '사업자 : ',
            'sw_pkg': 'PKG : ',
            'nfs': 'NF 지원 : ',
            'sess_5gm' : '5G mobile session수 : '
        }

SubsInlineFormSet = inlineformset_factory(Oppkg, Subscriber,
    fields = ['year', 'num_5gm', 'num_4gm', 'num_5gf'],
    extra = 3
)