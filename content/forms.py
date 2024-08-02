from django import forms
from .models import BlogComment

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ["comment", ]
        widgets = {
            "comment": forms.Textarea(attrs={"class": "form-control", "placeholder": "Comment", "style":"text-transform:none;",}),
        }
        