from django import forms
from .models import MyClient

class MyClientForm(forms.ModelForm):
    class Meta:
        model = MyClient
        fields = [  # генератор-выражение, формирующее список полей нашеё таблицы для отображения в админке
            field.name for field in MyClient._meta.fields if field.name not in (
                "id", "tgid")]

