from django import forms

class CpfPlanning(forms.Form):
    DATE_RECEIVE = forms.CharField(required=True,label = "Date Recieving")
    FACTORY = forms.CharField(required=True,label = "CPF Factory")
    PRODUCT = forms.CharField(required=True,label = "Product Detail")
    VOLUME = forms.CharField(required=True,label = "Quantity")