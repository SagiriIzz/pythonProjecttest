from django import forms

class Znach(forms.Form):
    inp0 = forms.IntegerField('знач0', default=0)
    inp1 = forms.IntegerField('знач1', default=0)
    inp2 = forms.IntegerField('знач2', default=0)
