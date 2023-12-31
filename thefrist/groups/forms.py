from django.forms import ModelForm
from .models import Group

class GroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description']
        
        
class GroupUpdateForm(ModelForm):
    class Meta:
        model = Group
        fields = ['name', 'description', 'owner']