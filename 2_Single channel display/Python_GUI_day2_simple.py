import dearpygui.dearpygui as dpg
from math import sin, cos

dpg.create_context()

sindatax = []
sindatay = []
for i in range(0, 500):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * sin(50 * i / 1000))

def update_series(j):

    cosdatax = []
    cosdatay = []
    print(j)
    for i in range(0, 500):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * cos(50 * (i+j) / 1000))
    dpg.set_value('series_tag', [cosdatax, cosdatay])
    dpg.set_item_label('series_tag', "0.5 + 0.5 * cos(x)")

with dpg.window(label="Window1", tag="win"):
    # create plot
    with dpg.plot(label="Line Series", height=300, width=600):
        # optionally create legend
        dpg.add_plot_legend()

        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

        # series belong to a y axis
        dpg.add_line_series(sindatax, sindatay, parent="y_axis", tag="series_tag")


dpg.create_viewport(title='Single channel display', width=600, height=400)
dpg.setup_dearpygui()
dpg.show_viewport()
i = 0
while dpg.is_dearpygui_running():
    i = i + 1
    update_series(i)
    dpg.render_dearpygui_frame()
dpg.destroy_context()