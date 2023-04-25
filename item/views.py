from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm


class IndexView(generic.TemplateView):
    template_name = 'index.html'


def capture(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item:capture')
    else:
        form = ItemForm()
    items = Item.objects.order_by('-created_at')
    context = {'items': items, 'form': form}
    return render(request, 'capture.html', context)

def update_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:capture')
    else:
        form = ItemForm(instance=item)
    context = {'form': form}
    return render(request, 'update_item.html', context)

def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item:capture')
    context = {'item': item}
    return render(request, 'delete_item.html', context)
