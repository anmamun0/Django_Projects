from django import forms
from .models import Post ,Comment
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = "__all__"
        exclude = ['author']
        widgets = {
             'title': forms.TextInput(attrs={
                'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 text-gray-800',
                'placeholder': 'Enter Blog Title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 text-gray-800',
                'placeholder': 'Write your content here...'
            }),
            'category': forms.SelectMultiple(attrs={
                'class': 'block w-full px-4 py-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500 text-gray-800',
            }),
            # 'category'
            # 'authors'
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model  = Comment 
        fields = ['name','email','body']