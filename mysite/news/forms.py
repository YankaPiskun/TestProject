from django import forms
from .models import Category, News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



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
        }

        def clean_title(self):
            title = self.cleaned_data['title']
            if re.match(r'\d', title):
                raise ValidationError('Название не должно начинаться с цифры')
            return title





