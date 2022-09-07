from django.forms import ModelForm
from .models import Stackmodel


class StackForm(ModelForm):
    class Meta:
        model = Stackmodel
        fields = '__all__'
        exclude=['content']
