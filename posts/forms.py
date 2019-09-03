from django import forms
from .models import PostModel
class PostForm(forms.ModelForm):
    
    class Meta:
        model = PostModel
        fields = ('title','image', 'content')
        labels = {
            'title':"Article",
            'content':'Content'
        }
        widgets = {
            'title' : forms.TextInput(attrs={
                    'class': 'form-control',
                    'placeholder': 'titre'
                      }),
            'content' : forms.Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'contenu'
                    }),
        }
