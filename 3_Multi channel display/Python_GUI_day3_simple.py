import dearpygui.dearpygui as dpg
# math is used to generate data for the plot widget
from math import cos,sin,tan

global SERIAL_TAG1
global SERIAL_TAG2
global SERIAL_TAG3

# The following function is used to generate and update the plot widget
# Here we generate separate data for each plot widget
def update_series(j):
    cosdatax1,cosdatax2,cosdatax3 = [[],[],[]]
    cosdatay1,cosdatay2,cosdatay3 = [[],[],[]]
    for i in range(0, 500):
        cosdatax1.append(i / 1000)
        cosdatax2.append(i / 1000)
        cosdatax3.append(i / 1000)
        cosdatay1.append(0.5 + 0.5 * cos(50 * (i+j) / 1000))
        cosdatay2.append(0.5 + 0.5 * sin(50 * (i+j) / 1000))
        cosdatay3.append(0.5 + 0.5 * tan(50 * (i+j) / 1000))
    """
    Pay attention
    When you plot data without GUI, you can use plt.plot(data)
    When you plot data with GUI, you need to use dpg.set_value() to update the data, the data will be shown
    in the plot widget with the tag "series_tag", this tag is assigned to the plot widget at line 41.
    """
    dpg.set_value(SERIAL_TAG1, [cosdatax1, cosdatay1])
    dpg.set_value(SERIAL_TAG2, [cosdatax2, cosdatay2])
    dpg.set_value(SERIAL_TAG3, [cosdatax3, cosdatay3])
    dpg.set_item_label(SERIAL_TAG1, "0.5 + 0.5 * cos(x)")
    dpg.set_item_label(SERIAL_TAG2, "0.5 + 0.5 * sin(x)")
    dpg.set_item_label(SERIAL_TAG3, "0.5 + 0.5 * tan(x)")

# The following function is used to start the GUI
def start_GUI():
    dpg.create_context()
    with dpg.window(label="Window1", tag="win"):

        # create the first plot widget
        with dpg.plot(label="Line Series1", height=200, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis1")

            # series belong to a y axis
            # We use the following codes to generate data for initialize plotting
            cosdatax = []
            cosdatay = []
            for i in range(0, 500):
                cosdatax.append(i / 1000)
                cosdatay.append(0.5 + 0.5 * cos(50 * (i) / 1000))
            dpg.add_line_series(cosdatax, cosdatay, parent="y_axis1", tag=SERIAL_TAG1)

        # create the second plot widget
        with dpg.plot(label="Line Series2", height=200, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis2")

            # series belong to a y axis
            # We use the following codes to generate data for initialize plotting
            cosdatax = []
            cosdatay = []
            for i in range(0, 500):
                cosdatax.append(i / 1000)
                cosdatay.append(0.5 + 0.5 * sin(50 * (i) / 1000))
            dpg.add_line_series(cosdatax, cosdatay, parent="y_axis2", tag=SERIAL_TAG2)

        # create the third plot widget
        with dpg.plot(label="Line Series3", height=200, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis3")

            # series belong to a y axis
            # We use the following codes to generate data for initialize plotting
            cosdatax = []
            cosdatay = []
            for i in range(0, 500):
                cosdatax.append(i / 1000)
                cosdatay.append(0.5 + 0.5 * tan(50 * (i) / 1000))
            dpg.add_line_series(cosdatax, cosdatay, parent="y_axis3", tag=SERIAL_TAG3)

    dpg.create_viewport(title='Multiple channel display', width=600, height=700)
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
    SERIAL_TAG1 = "series_tag1"
    SERIAL_TAG2 = "series_tag2"
    SERIAL_TAG3 = "series_tag3"
    start_GUI()