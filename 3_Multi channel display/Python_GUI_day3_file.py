import dearpygui.dearpygui as dpg
# numpy is used to read data from file
import numpy as np

global SERIAL_TAG1
global SERIAL_TAG2
global SERIAL_TAG3

# Here we read the three channel data from the file
def read_data():
    filename = 'Data/charis4.dat'
    datafile =open(filename, 'rb')
    dtype = np.dtype('int16')
    data = np.fromfile(datafile,dtype)
    ABP  = [(data[i]+2644)/91.5061 for i in range(0, len(data), 3)]
    ECG  = [(data[i]+392)/6081.8245 for i in range(1, len(data), 3)]
    ICP  = [(data[i]+5)/84.0552 for i in range(2, len(data), 3)]
    return ABP,ECG,ICP

# The following function is used to generate and update the plot widget
# Here we use three series to display three signals
def update_series(j,ABP,ECG,ICP):
    dataxABP,dataxECG,dataxICP = [[],[],[]]
    datayABP,datayECG,datayICP = [[],[],[]]
    for i in range(0, 500):
        # Here we divide i by 50 to get the real time in seconds
        dataxABP.append(i / 50)
        dataxECG.append(i / 50)
        dataxICP.append(i / 50)
    datayABP = ABP[j:j+500]
    datayECG = ECG[j:j+500]
    datayICP = ICP[j:j+500]
    dpg.set_value(SERIAL_TAG1, [dataxABP, datayABP])
    dpg.set_value(SERIAL_TAG2, [dataxECG, datayECG])
    dpg.set_value(SERIAL_TAG3, [dataxICP, datayICP])
    dpg.set_item_label(SERIAL_TAG1,'Arterial Blood Pressure')
    dpg.set_item_label(SERIAL_TAG2,'Electrocardiogram')
    dpg.set_item_label(SERIAL_TAG3,'Intracranial Pressure')

# The following function is used to start the GUI
def start_GUI(ABP,ECG,ICP):
    dpg.create_context()
    with dpg.window(label="Window1", tag="win"):

        # create plot
        with dpg.plot(label="Channel 1", height=200, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="time")
            dpg.add_plot_axis(dpg.mvYAxis, label="amplitude/mmHg", tag="y_axis1")

            # series belong to a y axis
            dpg.add_line_series(np.arange(0,500), np.zeros(500), parent="y_axis1", tag=SERIAL_TAG1)

        with dpg.plot(label="Channel 2", height=200, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="time")
            dpg.add_plot_axis(dpg.mvYAxis, label="amplitude/mV", tag="y_axis2")

            # series belong to a y axis
            dpg.add_line_series(np.arange(0,500), np.zeros(500), parent="y_axis2", tag=SERIAL_TAG2)

        with dpg.plot(label="Channel 3", height=200, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="time")
            dpg.add_plot_axis(dpg.mvYAxis, label="amplitude/mmHg", tag="y_axis3")

            # series belong to a y axis
            dpg.add_line_series(np.arange(0,500), np.zeros(500), parent="y_axis3", tag=SERIAL_TAG3)

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
        update_series(i,ABP,ECG,ICP)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":
    SERIAL_TAG1 = "series_tag1"
    SERIAL_TAG2 = "series_tag2"
    SERIAL_TAG3 = "series_tag3"
    ABP,ECG,ICP = read_data()
    start_GUI(ABP,ECG,ICP)