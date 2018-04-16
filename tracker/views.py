from django.shortcuts import render, redirect
from django.contrib import admin
from .models import Item
from .forms import ItemForm


admin.site.register(Item)


def tracker(request):
    results = Item.objects.all()
    return render(request, "tracker.html", {'items': results})

def create_a_bug(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(tracker)
    else:
        form = ItemForm()

    return render(request, "issueform.html", {'form': form})










