import dearpygui.dearpygui as dpg
# numpy and math are used to generate data for the plot widget
import numpy as np

global SERIAL_TAG

# The following codes are used to read data from a file. We will use ICP as an example.
def read_data():
    filename = 'Data/charis4.dat'
    datafile =open(filename, 'rb')
    dtype = np.dtype('int16')
    data = np.fromfile(datafile,dtype)
    ICP  = [(data[i]+5)/84.0552 for i in range(2, len(data), 3)]
    return ICP

# The following codes are used to update the plot widget
# It is the same as the codes in previous example. The only difference is that we replace the random data with ICP data.
def update_series(j,ICP):
        datax = []
        datay = []
        for i in range(0, 500):
            # Here we divide i by 50 to get the real time in seconds
            datax.append(i / 50)
        datay = ICP[j:j+500]
        dpg.set_value(SERIAL_TAG, [datax, datay])
        dpg.set_item_label(SERIAL_TAG,'Intracranial Pressure')

# The following codes are used to start the GUI
def start_GUI(ICP):
    dpg.create_context()

    with dpg.window(label="Window1", tag="win"):
        # create plot
        with dpg.plot(label="Arterial blood pressure", height=300, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="time/s", tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="y/mmHg", tag="y_axis")

            # series belong to a y axis
            dpg.add_line_series(np.arange(0,500), np.zeros(500), parent="y_axis", tag=SERIAL_TAG)

    dpg.create_viewport(title='Single channel display', width=600, height=400)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    i = 0
    while dpg.is_dearpygui_running():
        # When read data from file, we need to ensure that the data is not out of range.
        if i >= len(ICP):
            i = 0
        i = i + 1
        update_series(i,ICP)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":
    SERIAL_TAG = "series_tag"
    # The following codes start the GUI
    ICP = read_data()
    start_GUI(ICP)