from django import forms
from .models import Category, News


class NewsForm(forms.ModelForm):
    # title = forms.CharField(max_length=250, label='Название:', widget=forms.TextInput(attrs={"class": "form-control"}))
    # content = forms.CharField(label='Текст:', required=False, widget=forms.Textarea(attrs={"class": "form-control",
    #                                                                                        "rows": 5}))
    # is_published = forms.BooleanField(label='Оппубликовано:', required=False, initial=True)
    # category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Категории:',
    # empty_label='Выбериет категорию', widget=forms.Select(attrs={"class": "form-control"}))
    # photo = forms.ImageField(label='Загрузите фото')
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content': forms.Textarea(attrs={"class": "form-control", 'rows': 5}),
            'category': forms.Select(attrs={"class": "form-control"}),
            'title': forms.TextInput(attrs={"class": "form-control"}),
        }



