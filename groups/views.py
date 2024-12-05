from django.shortcuts import render, get_object_or_404, redirect
from .models import Group

def group_list(request):
    groups = Group.objects.all()
    return render(request, 'groups/group_list.html', {'groups': groups})

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/group_detail.html', {'group': group})

def group_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        group_type = request.POST['type']
        Group.objects.create(name=name, type=group_type)
        return redirect('groups:group_list')
    return render(request, 'groups/group_form.html')

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:group_list')
