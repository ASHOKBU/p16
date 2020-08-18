from django.shortcuts import render
from myapp import forms
# Create your views here.
def builtinforms(request):
    form=forms.SampleForm()
    return render(request,'builtinform.html',{'form':form})