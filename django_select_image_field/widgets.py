from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.utils.encoding import force_text
from itertools import chain
from django.forms.utils import flatatt

class SelectImgWidget(forms.Select):

    def render_options(self, selected_choices):
        # Normalize to strings.
        selected_choices = set(force_text(v) for v in selected_choices)
        output = []
        for option_value, option_label, option_image in self.choices:

            if isinstance(option_label, (list, tuple)):
                output.append(format_html('<optgroup label="{}">', force_text(option_value)))
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
                output.append('</optgroup>')
            else:
                output.append(self.render_option(selected_choices, option_value, option_label, option_image))
        return '\n'.join(output)

    # def render_options(self, choices, selected_choices):
    #     # Normalize to strings.
    #     selected_choices = set(force_text(v) for v in selected_choices)
    #     output = []
    #     for option_value, option_label, option_image in chain(self.choices, choices):
    #         if isinstance(option_label, (list, tuple)):
    #             output.append(format_html('<optgroup label="{}">', force_text(option_value)))
    #             for option in option_label:
    #                 output.append(self.render_option(selected_choices, *option))
    #             output.append('</optgroup>')
    #         else:
    #             output.append(self.render_option(selected_choices, option_value, option_label, option_image))
    #     return '\n'.join(output)

    def render_option(self, selected_choices, option_value, option_label, option_image):
        if option_value is None:
            option_value = ''
        option_value = force_text(option_value)
        if option_value in selected_choices:
            selected_html = mark_safe(' selected="selected"')
            if not self.allow_multiple_selected:
                # Only allow for a single selection.
                selected_choices.remove(option_value)
        else:
            selected_html = ''
        return format_html('<option value="{}" data-image="/{}" {}>{} </option>',
                           option_value,
                           option_image,
                           selected_html,
                           force_text(option_label))
