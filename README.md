# DJANGO SELECT-IMAGE FIELD

<snippet>
  <content>

[![Build Status](https://travis-ci.org/Chive/django-multiupload.svg?branch=master)](https://travis-ci.org/Chive/django-multiupload)


A dropdown(with images) field that uses django's ```forms.ChoiceField()``` and ```msdropdown``` to stylize and create the field. 

## Installation

* Install the package using pip (or easy_install if you really have to)

```bash
$ pip install django_select_image_field
```

## Usage

An example app is avilable at [example app](https://github.com/shakle17/django_select_image_field/tree/master/test_select_image).


Since we use ```jquery``` and ```msdropdown (js & css)``` for the widget , you need to include them in your main template (or the template where the widget will be rendered)

```javascript
<!-- templates/base.html -->

<!-- You should include jquery and msdropdown (js & css ) -->
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script src="http://www.marghoobsuleman.com/mywork/jcomponents/image-dropdown/samples/js/msdropdown/jquery.dd.min.js"></script>
<link rel="stylesheet" href="http://www.marghoobsuleman.com/mywork/jcomponents/image-dropdown/samples/css/msdropdown/dd.css">
<!-- alternativly my suggestion is to use the modified version of the css file ( dd.css ) that you can find in test_select_image/static/msdropdown/dd.css -->

</head>

<!-- Anywhere in the body section, you have to include this block code -->

<script language="javascript">
  $(document).ready(function(e) {
    $(".select-img").msDropDown();
  });
</script>

```

Add the form field to your form ( since we use django's forms.ChoiceField() we pass choices as a tuple (value,text,image source) for each option in the select-dropdown ).

```python
# forms.py
from django import forms
from django_range_slider.fields import RangeSliderField

COUNTRIES = (
    ('0','Macedonia','static/images/mk.png'),
    ('1','Hungary','static/images/hu.png'),
    ('2','Ireland','static/images/ir.jpg'),
    ('3','Ecuador','static/images/ec.png'),
    ('4','Slovenia','static/images/si.png'),
)


class CountriesForm(forms.Form):

    name = SelectImageField(choices=COUNTRIES)

    def __init__(self, *args, **kwargs):
        super(CountriesForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'select-img' # select-img class is used to mark the field as SELECT-IMAGE
```


## Example field

This an example field that is used in the test_select_image app
NOTE: For this field it's not used the default dd.css file from the msdropdown, instead it's used the test_select_image/static/msdropdown/dd.css file

![select-image field](https://s27.postimg.org/i9xa4grb7/Screenshot_from_2017_01_26_02_56_44.png)


## License
MIT License

Copyright (c) 2016 Aleksandar Shaklev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

</content>
</snippet>
