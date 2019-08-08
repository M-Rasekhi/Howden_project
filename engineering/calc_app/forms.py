from django import forms
from .models import Rectangle, FanUnbalance, EarthQuake


class RectangleForm(forms.ModelForm):
    class Meta():
        model = Rectangle
        fields = '__all__'


class FanUnbalanceForm(forms.ModelForm):
    class Meta():
        model = FanUnbalance
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['balance_grade'].widget.attrs.update({'class': 'special'})
        self.fields['impeller_mass'].widget.attrs.update({'class': 'special'}, size='200')


class EarthQuakeForm(forms.ModelForm):
    class Meta():
        model = EarthQuake
        fields = '__all__'

            #   <!-- <div class="col-6">
            #      {{ form.site_class|as_crispy_field }}
            #   </div> -->
            #   <!-- <div class="col-6">
            #       {{ form.res_mod_coeff|as_crispy_field }}
            #    </div> -->
            #    <!-- <div class="col-6">
            #       {{ form.risk_cat|as_crispy_field }}
            #    </div> -->
            #    <!-- <div class="col-6">
            #       {{ form.s1|as_crispy_field }}
            #    </div> -->
            #    <!-- <div class="col-6">
            #       {{ form.ss|as_crispy_field }}
            #    </div> -->
            #    <!-- <div class="col-6">
            #       {{ form.fund_period|as_crispy_field }}
            #    </div> -->
            #    <!-- <div class="col-6">
            #       {{ form.long_period|as_crispy_field }}
            #    </div> -->