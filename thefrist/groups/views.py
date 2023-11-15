from django.shortcuts import render

groups_list = [
    {'id': 0, 'name': 'Group 0'},
    {'id': 1, 'name': 'Group 1'},
    {'id': 2, 'name': 'Group 2'},
    {'id': 3, 'name': 'Group 3'},
]

def groups(request):
    context = {'groups_list': groups_list}
    return render(request, 'groups/index.html', context)

def group_detail(request, group_id):
    group = groups_list[group_id]
    context = {'group': group}
    return render(request, 'groups/group_detail.html', context)