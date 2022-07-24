from django import forms
from books.models import Nf, Oppkg

class NfForm(forms.ModelForm):
    class Meta:
        model = Nf
        fields = ['name']


class OppkgForm(forms.ModelForm):
    class Meta:
        model = Oppkg
        fields = ['operator','sw_pkg','nfs','comment']
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class': 'form-control'}),
        #     'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        # }
        labels = {
            'operator': '사업자',
            'sw_pkg': 'PKG',
            'nfs': 'NF 지원',
        }

