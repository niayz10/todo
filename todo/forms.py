from django import forms


from .models import Item


class ToDoTitleForm(forms.Form):
    title = forms.CharField(label="Title", max_length=100)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',

            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание',
                'rows': 4,
            }),
        }
        labels = {
            'title': 'Название',
            'description': 'Описание',
        }