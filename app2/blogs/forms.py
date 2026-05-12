from django import forms
from .models import BlogDb
class Postform(forms.ModelForm):
    blogauthor=forms.CharField(widget=forms.TextInput(attrs={"id":"ba","value":"","type":"hidden"}))
    class Meta:
        model=BlogDb
        fields=["blogtitle","blogcontent","blogauthor","picture"]
        # fields"__all__"