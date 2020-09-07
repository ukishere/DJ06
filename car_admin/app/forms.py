from django import forms
from .models import Review

from ckeditor.widgets import CKEditorWidget


class ReviewAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Review
        fields = ['car', 'title', 'text']

# class ReviewAdminForm(forms.ModelForm):
#     text = forms.CharField(widget=CKEditorWidget(), label='Текст')
#
#     class Meta:
#         model = Review
#         fields = ['car', 'title', 'text']