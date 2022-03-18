import pickle
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.

def index(request):
    if request.method == 'GET':
        form = MobileForm()
        return render(request, 'index.html', context={'form': form})
    if request.method == 'POST':
        form = MobileForm(request.POST)
        if form.is_valid():
            param = get_price(form.cleaned_data['battery_power'], form.cleaned_data['blue'],
                              form.cleaned_data['clock_speed'],
                              form.cleaned_data['dual_sim'], form.cleaned_data['fc'],
                              form.cleaned_data['four_g'], form.cleaned_data['int_memory'],
                              form.cleaned_data['m_dep'], form.cleaned_data['mobile_wt'], form.cleaned_data['n_cores'],
                              form.cleaned_data['pc'], form.cleaned_data['px_height'], form.cleaned_data['px_width'],
                              form.cleaned_data['ram'], form.cleaned_data['sc_h'], form.cleaned_data['sc_w'],
                              form.cleaned_data['talk_time'], form.cleaned_data['three_g'],
                              form.cleaned_data['touch_screen'],
                              form.cleaned_data['wifi'])
            return render(request, 'result.html', context={'param': param})
        return render(request, 'index.html', context={'form': form})


def get_price(battery_power, blue, clock_speed, dual_sim, fc, four_g, int_memory, m_dep, mobile_wt, n_cores, pc,
              px_height, px_width, ram, sc_h, sc_w, talk_time, three_g, touch_screen, wifi):
    model = pickle.load(open('ml_model.sav', 'rb'))
    prediction = model.predict(
        [[battery_power, int(blue), clock_speed, int(dual_sim), fc, int(four_g), int_memory, m_dep, mobile_wt, n_cores,
          pc, px_height,
          px_width, ram, sc_h, sc_w, talk_time, int(three_g), int(touch_screen), int(wifi)]])
    if 0 <= prediction <= 3:
        return int(prediction)
    else:
        return 'error'
