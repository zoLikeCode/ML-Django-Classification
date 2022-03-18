from django import forms
from .models import *


class MobileForm(forms.Form):
    battery_power = forms.IntegerField(label='Buttery power',
                                       validators=[MinValueValidator(500), MaxValueValidator(1999)],
                                       widget=forms.TextInput(attrs={'class': 'form-control'}))
    blue = forms.BooleanField(label='Bluetooth', initial=False, required=False,
                              widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    clock_speed = forms.FloatField(label='Clock speed', validators=[MinValueValidator(0.5), MaxValueValidator(3)],
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    dual_sim = forms.BooleanField(label='Dual sim', initial=False, required=False,
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    fc = forms.IntegerField(label='From camera', validators=[MinValueValidator(0), MaxValueValidator(19)],
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    four_g = forms.BooleanField(label='4G', initial=False, required=False,
                                widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    int_memory = forms.IntegerField(label='Internal Memory (gb)',
                                    validators=[MinValueValidator(2), MaxValueValidator(64)],
                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    m_dep = forms.FloatField(label='Mobile Depth (cm)', validators=[MinValueValidator(0.1), MaxValueValidator(1)],
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_wt = forms.IntegerField(label='Mobile weight', validators=[MinValueValidator(80), MaxValueValidator(200)],
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    n_cores = forms.IntegerField(label='Cores of processor', validators=[MinValueValidator(1), MaxValueValidator(8)],
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    pc = forms.IntegerField(label='Primary Camera', validators=[MinValueValidator(0), MaxValueValidator(20)],
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    px_height = forms.IntegerField(label='Pixel Resolution Height',
                                   validators=[MinValueValidator(0), MaxValueValidator(1907)],
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    px_width = forms.IntegerField(label='Pixel Resolution Width',
                                  validators=[MinValueValidator(501), MaxValueValidator(1998)],
                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    ram = forms.IntegerField(label='Random Access Memory in Megabytes',
                             validators=[MinValueValidator(263), MaxValueValidator(3989)],
                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    sc_h = forms.IntegerField(label='Screen Height of mobile in cm',
                              validators=[MinValueValidator(5), MaxValueValidator(19)],
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    sc_w = forms.IntegerField(label='Screen Width of mobile in cm',
                              validators=[MinValueValidator(0), MaxValueValidator(18)],
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    talk_time = forms.IntegerField(label='Talk Time', validators=[MinValueValidator(2), MaxValueValidator(20)],
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    three_g = forms.BooleanField(label='3G', initial=False, required=False,
                                 widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    touch_screen = forms.BooleanField(label='Touch Screen', initial=False, required=False,
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    wifi = forms.BooleanField(label='WiFi', initial=False, required=False,
                              widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
