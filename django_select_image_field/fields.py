from django import forms
from select_image.widgets import SelectImgWidget

class SelectImageField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['widget'] = SelectImgWidget()
        super(SelectImageField, self).__init__(*args, **kwargs)
