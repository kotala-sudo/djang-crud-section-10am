from django import forms
from .models import Employee

class AddEmployeeForm(forms.ModelForm):
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'First Name'
    }))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Last Name'
    }))
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={
        'class' : 'form-control',
        'placeholder' : 'Email'
    }))

    class Meta:
        model = Employee
        fields = "__all__"