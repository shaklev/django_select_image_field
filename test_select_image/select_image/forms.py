from django import forms
from .fields import SelectImageField
from django_select_image_field.fields import SelectImageField

COUNTRIES = (
    ('0','Macedonia','static/images/mk.png'),
    ('1','Hungary','static/images/hu.png'),
    ('2','Ireland','static/images/ir.jpg'),
    ('3','Ecuador','static/images/ec.png'),
    ('4','Slovenia','static/images/si.png'),
)


class CountriesForm(forms.Form):

    name = SelectImageField(choices=COUNTRIES)
    surname = SelectImageField(choices=COUNTRIES)

    def __init__(self, *args, **kwargs):
        super(CountriesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'select-img form-control'
        self.fields['surname'].widget.attrs['class'] = 'select-img form-control'
