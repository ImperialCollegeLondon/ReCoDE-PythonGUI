import dearpygui.dearpygui as dpg
# numpy and math are used to generate data for the plot widget
import numpy as np

SERIAL_TAG = "series_tag"

# The following codes are used to read data from a file. We will use ICP as an example.
def read_data():
    """ read data from file
    This function is used to read data from a file.
    The data is stored in a file named charis4.dat under Data folder.
    The data is stored in the following format:
    1st data point: first data of ABP
    2nd data point: first data of ECG
    3rd data point: first data of ICP
    4th data point: second data of ABP
    5th data point: second data of ECG
    6th data point: second data of ICP
    ...

    return:
        ICP: the data of ICP

    """
    filename = 'Data/charis4.dat'
    with open(filename, 'rb') as datafile:
        data = np.fromfile(datafile, np.dtype('int16'))
    ICP  = (data[2::3]+5)/84.0552
    return ICP

# The following codes are used to update the plot widget
# It is the same as the codes in previous example. The only difference is that we replace the random data with ICP data.
def update_series(j,ICP):
    """update data for plotting
    This function is used to update data from files for plotting.
    when you display data dynamically, you need to specify the length of the data
    in this case, the length of the data is 500, that is, there are 500 points in the plot widget
    
    Args:
        j: the index of the data
        ICP: the data of ICP
    """
    datax = np.arange(500)/50
    datay = ICP[j:j+500]
    dpg.set_value(SERIAL_TAG, [datax, datay])
    dpg.set_item_label(SERIAL_TAG,'Intracranial Pressure')


def create_window():
    """ create a window
    This function is used to create a window
    This window contains several widgets like buttons, checkboxes, texts... 
	as well as an static plot to illustrate the capabilities of dearpygui.
	
	For each widget, parameter pos=[x,y] (x is the horizontal position and 
	y is the vertical position) can be used to set the position of the widget. 
	If not set, the widget will be placed automatically. In this case, the 
	radio button will be set below the checkbox widgets rather than side by side.
    """

    """
    In Python, the with statement is used for working with objects that support a context manager protocol. 
    It ensures that resources are properly managed and cleaned up when they are no longer needed. Here,
    the with statement is used to create a window and all the widgets added to the window will be automatically
    added to the window. The same for when you create a menu bar and plot widget.
    """ 
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

    
def start_dearpygui(ICP):
    """ update the GUI frame by frame
    Here we change dpg.start_dearpygui() to while dpg.is_dearpygui_running() and dpg.render_dearpygui_frame()
    This is because we want to update the plot widget in a loop, if we use dpg.start_dearpygui(), the GUI will
    be frozen and the plot widget will not be updated.

    Args:
        ICP: the data of ICP

    """    
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

    # The following codes start the GUI
    dpg.create_context()
    dpg.create_viewport(title='Single channel display', width=600, height=400)

    # The following codes are custom functions to create windows and read data from files
    create_window()
    ICP = read_data()

    # The setup_dearpygui() function is used to setup the viewport.
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # As we will manually render the frame, we do not need to use dpg.start_dearpygui(). We used a customized function instead.
    start_dearpygui(ICP)
    # All dearpygui apps end with destroy_context()
    dpg.destroy_context()