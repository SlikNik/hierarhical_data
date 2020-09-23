from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from data.models import Data
from data.forms import AddDataForm

def index_view(request):
    return render(request, 'index.html', {'data': Data.objects.all()})

@login_required
def owner_view(request):
    return render(request, 'index.html', {"data": Data.objects.filter(created_by= request.user)})

@login_required
def add_data(request):
    if request.method == "POST":
        form = AddDataForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_data = Data.objects.create(
                name=data.get('name'),
                parent=data.get('parent'),
                created_by=request.user
            )
            return HttpResponseRedirect(reverse('ownerprofile'))
    form = AddDataForm()
    return render(request, 'generic_form.html', {'form': form})
