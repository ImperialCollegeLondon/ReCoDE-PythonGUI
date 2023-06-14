import dearpygui.dearpygui as dpg
# math is used to generate data for the plot widget
from math import cos

global SERIAL_TAG

# The following function is used to generate and update the plot widget
def update_series(j):
    cosdatax = []
    cosdatay = []
    for i in range(0, 500):
        cosdatax.append(i / 1000)
        cosdatay.append(0.5 + 0.5 * cos(50 * (i+j) / 1000))
    """
    Pay attention
    When you plot data without GUI, you can use plt.plot(data)
    When you plot data with GUI, you need to use dpg.set_value() to update the data, the data will be shown
    in the plot widget with the tag "series_tag", this tag is assigned to the plot widget at line 41.
    """
    dpg.set_value(SERIAL_TAG, [cosdatax, cosdatay])
    dpg.set_item_label(SERIAL_TAG, "0.5 + 0.5 * cos(x)")

# The following function is used to start the GUI
def start_GUI():
    dpg.create_context()
    with dpg.window(label="Window1", tag="win"):
        # create plot
        with dpg.plot(label="Line Series", height=300, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

            # series belong to a y axis
            # We use the following codes to generate data for initialize plotting
            cosdatax = []
            cosdatay = []
            for i in range(0, 500):
                cosdatax.append(i / 1000)
                cosdatay.append(0.5 + 0.5 * cos(50 * (i) / 1000))
            dpg.add_line_series(cosdatax, cosdatay, parent="y_axis", tag=SERIAL_TAG)

    dpg.create_viewport(title='Single channel display', width=600, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    i = 0
    """
    Here we change dpg.start_dearpygui() to while dpg.is_dearpygui_running() and dpg.render_dearpygui_frame()
    This is because we want to update the plot widget in a loop, if we use dpg.start_dearpygui(), the GUI will
    be frozen and the plot widget will not be updated.
    """
    while dpg.is_dearpygui_running():
        i = i + 1
        update_series(i)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":
    SERIAL_TAG = "series_tag"
    start_GUI()