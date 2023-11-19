from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def groups(request):
    groups_list = Group.objects.all()
    context = {'groups_list': groups_list}
    return render(request, 'groups/index.html', context)

def detail(request, id):
    group = Group.objects.get(id=id)    
    context = {'group': group, 'id': group.id}
    return render(request, 'groups/detail.html', context)


def create(request):
    
    if not request.user.is_authenticated:
        return redirect('/admin/login')
    
    form = GroupForm(request.POST or None)
    
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.owner = request.user
            group.save()
            return redirect('/groups')
    
    context = {'form': form}
    return render(request, 'groups/create.html', context)

def update(request, id):
    
    if not request.user.is_authenticated:
        return redirect('/admin/login')
    
    group = get_object_or_404(Group, id=id)
    form = GroupUpdateForm(request.POST or None, instance=group)
    
    if request.method == 'POST':
        form = GroupUpdateForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('/groups')
    
    context = {'form': form, 'id': group.id}
    return render(request, 'groups/update.html', context)

def delete(request, id):
    
    if not request.user.is_authenticated:
        return redirect('/admin/login')
    
    group = Group.objects.get(id=id)
    
    if request.method == 'POST':
        group.delete()
        return redirect('/groups')
    
    context = {'group': group}
    return render(request, 'groups/delete.html', context)