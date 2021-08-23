from django import forms
from .models import User, Post


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields= ['first_name', 'username', 'email']

class PostForm(forms.Form):
    class Meta:
        model = Post
        fields= '__all__'

    
