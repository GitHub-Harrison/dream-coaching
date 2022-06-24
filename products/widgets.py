from django import forms


class DatePicker(forms.DateInput):
    """ widget for picking date """

    input_type = 'date'
