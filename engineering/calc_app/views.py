from django.shortcuts import render
from calc_app.forms import RectangleForm, FanUnbalanceForm, EarthQuakeForm
from lib.rectangle_properties import Rect
from lib.fan_unbalance import Fan
from lib.earthquake_load import Quake
from . models import Rectangle, FanUnbalance, EarthQuake

# Create your views here.


def index(request):
    return render(request, 'index.html')


def rectangle(request):

    form = RectangleForm()

    if request.method == 'POST':
        form = RectangleForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            x = float(form.cleaned_data['rec_width'])
            y = float(form.cleaned_data['rec_height'])

            arta = Rect(x, y)
            result1 = arta.area()
            result2 = round(arta.p_moment(), 2)
            result3 = "Area = "
            result4 = "Principal Moment of Inertia = "

            return render(request, 'section_prop.html', {'form': form, 'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4})
        else:
            print('Form Invalid')

    return render(request, 'section_prop.html', {'form': form})


def fan_unbalance(request):
    form = FanUnbalanceForm()

    if request.method == 'POST':
        form = FanUnbalanceForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            A = float(form.cleaned_data['balance_grade'])
            B = float(form.cleaned_data['impeller_mass'])
            C = float(form.cleaned_data['fan_speed'])
            D = float(form.cleaned_data['backplate_dia'])

            fan = Fan(A, B, C, D)
            result1 = fan.pru()
            result2 = fan.patch_area()
            result3 = "Premissable Residual Unbalance = "
            result4 = "Max. Patch Area = "

            return render(request, 'fan_unbalance.html', {'form': form, 'result1': result1, 'result2': result2, 'result3': result3, 'result4': result4})
        else:
            print('Form Invalid')

    return render(request, 'fan_unbalance.html', {'form': form})

def earth_quake(request):
    form = EarthQuakeForm()

    if request.method == 'POST':
        form = EarthQuakeForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            A = form.cleaned_data['site_class']
            B = float(form.cleaned_data['res_mod_coeff'])
            C = int(form.cleaned_data['risk_cat'])
            D = float(form.cleaned_data['ss'])
            E = float(form.cleaned_data['s1'])
            F = float(form.cleaned_data['fund_period'])
            G = float(form.cleaned_data['long_period'])
            H = float(form.cleaned_data['height'])
            I = form.cleaned_data['structure_type']
            J = form.cleaned_data['site_class_calculated']
            

            quake = Quake(A, B, C, D, E, F, G, H, I, J)
            result1 = quake.importance_factor()
            result2 = quake.fa()
            result3 = quake.fv()
            result4 = quake.sm_one()
            result5 = quake.sm_s()
            result6 = quake.sd_one()
            result7 = quake.sd_s()
            result8 = quake.cs()
            result9 = quake.cu()
            result10 = quake.ct()
            result11 = quake.x()
            result12 = quake.seismic_design_cat()
            result13 = quake.fv_warning()
            result14 = quake.ta()
            



            return render(request, 'earthquake_load.html', {'form': form, 'result1': result1, 'result2': result2, 'result3': result3,
             'result4': result4, 'result5': result5, 'result6': result6,
              'result7': result7, 'result8': result8, 'result9': result9,
              'result10': result10, 'result11': result11, 'result12': result12, 'result13': result13, 'result14': result14})
            # return render(request, 'earthquake_load.html', {'form': form,'result8': result8})
        else:
            print('Form Invalid')

    return render(request, 'earthquake_load.html', {'form': form})


# def wind(request):
