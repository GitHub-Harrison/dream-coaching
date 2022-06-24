from .widgets import DatePicker
from .models import Product


class DateInput(forms.Form):
    input_type = 'date'


class DatePickerInput(forms.Form):

    class Meta:
        model = Product
        fields = 'date'
        widgets = {
            'date': DatePicker()
        }
