import dearpygui.dearpygui as dpg
import numpy as np

from math import sin, cos

dpg.create_context()

sindatax = []
sindatay = []
for i in range(0, 500):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))
filename = 'charis4.dat'
datafile =open(filename, 'rb')
dtype = np.dtype('int16')
data = np.fromfile(datafile,dtype)
ABP  = [data[i]/91.5061 for i in range(0, len(data), 3)]

def update_series(j,ABP):

    datax = []
    datay = []
    for i in range(0, 500):
        datax.append(i / 1000)
    datay = ABP[j:j+500]
    dpg.set_value('series_tag', [datax, datay])
    dpg.set_item_label('series_tag','ABP')

with dpg.window(label="Window1", tag="win"):
    # create plot
    with dpg.plot(label="Arterial blood pressure", height=300, width=600):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y/mmHg", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(sindatax, sindatay, parent="y_axis", tag="series_tag")


dpg.create_viewport(title='Single channel display', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
i = 0
while dpg.is_dearpygui_running():
    i = i + 1
    update_series(i,ABP)
    dpg.render_dearpygui_frame()
dpg.destroy_context()