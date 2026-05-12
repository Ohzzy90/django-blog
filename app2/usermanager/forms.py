from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from usermanager.models import ProfileModel, Comment,Like

class Newuserform(UserCreationForm):
    first_name=forms.CharField(max_length=50, required=True)
    last_name=forms.CharField(max_length=50, required=True)
    email=forms.EmailField(max_length=100, required=True)
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

    def save(self,*args,**kwargs):
        return super(Newuserform,self).save(*args,**kwargs)
        

    # def save(self,commit=True):
    #     super(Newuserform,self).save(commit=False)
    #     Newuserform.cleaned_data.get("first_name")    
    #     Newuserform.cleaned_data.get("last_name")    
    #     Newuserform.cleaned_data.get("email")
    #     if commit:
    #         return Newuserform.save()        

class Profileform(forms.ModelForm):
    # first_name=forms.CharField(max-length=200,required=True)
    # last_name=forms.CharField(max-length=200,required=True)
    # email=forms.EmailField(max-length=200,required=True)
    class Meta:
        model=ProfileModel
        fields=["profile_pic","bio","facebook","instagram"]

class Edituserform(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","first_name","last_name","email"]

class commentform(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["content"]

class likeform(forms.ModelForm):
    class Meta:
        model=Like
        fields=["react"]

  