from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm


def features(request):
    results = Item.objects.all()
    return render(request, 'features.html', {'items': results})


@login_required
def create_a_feature(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect(features)
    else:
        form = ItemForm()

    return render(request, "itemform.html", {'form': form})
