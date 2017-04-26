from django.shortcuts import render
from basicapp import forms


def index(request):
    return render(request, 'basicapp/index.html')
# Create your views here.
def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("VALDIATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
    return render (request,'basicapp/form_page.html',{'form':form})
