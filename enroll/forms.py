from django import forms
from .models import Student
from django.core.exceptions import ValidationError


class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields=['stuname','stuemail','stupass']
        labels={'stuname':'Enter Name','stuemail':'Enter Email','stupass':'Enter Password'}
        # help_text={'stuname':'Provide Full Name'}
        widgets={
            'stuname':forms.TextInput(attrs={'class':'form-control'}),
            'stuemail':forms.EmailInput(attrs={'class':'form-control'}),
            'stupass':forms.PasswordInput(attrs={'class':'form-control'}),
        }


#forms 