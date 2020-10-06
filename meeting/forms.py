from django import forms

class meetingCreate(forms.Form):
    date = forms.CharField(label="", required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.CharField(max_length=10, required=False,)
