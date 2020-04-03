from django import forms


class WineForm(forms.Form):
    comments = forms.CharField(label='Comments', max_length=2000, widget=forms.Textarea(attrs={"rows": 3,
                                                                                               "class":
                                                                                                   "form-control"}))
    score = forms.FloatField(label='Score', widget=forms.NumberInput(attrs={"max": 5, "class": "form-control",
                                                                            "min": 0}))
    tags = forms.CharField(label='Tags', required=False, max_length=2000,
                           widget=forms.TextInput(attrs={"class": "form-control"}))
