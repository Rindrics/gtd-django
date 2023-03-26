from django.views import generic
from django.shortcuts import render, redirect
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
