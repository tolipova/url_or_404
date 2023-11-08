from django import forms
from .models import Users, Posts

class UserForms(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'

class PostForms(forms.ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'
        widgets = {
            'category': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control'}),
            'info': forms.TextInput(attrs={'class':'form-control'})

        }