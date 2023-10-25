from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
   
    class Meta:
        model = Member
        fields = '__all__'
        exclude = ['subscription_renewal_date', 'membership_end_date']
        widgets = {'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'age': forms.NumberInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'phone': forms.NumberInput(attrs={'class': 'form-control'}),
                   'place': forms.TextInput(attrs={'class': 'form-control'}),
                   'subscription_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'subscription_renewal_date': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'auto-generated'}),
                   'membership_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
                   'membership_end_date': forms.DateInput(attrs={'class': 'form-control', 'readonly': 'readonly', 'placeholder': 'auto-generated'})
                   }
