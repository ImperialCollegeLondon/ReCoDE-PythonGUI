import dearpygui.dearpygui as dpg
# numpy is used to read data from file
import numpy as np

# define the tags for each plot widget
TAGS = "series_tag1", "series_tag2", "series_tag3"

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
        ABP: the data of ABP
        ECG: the data of ECG
        ICP: the data of ICP

    """
    filename = 'Data/charis4.dat'
    with open(filename, 'rb') as datafile:
        data = np.fromfile(datafile, np.dtype('int16'))
    ABP  = (data[0::3]+2644)/91.5061
    ECG  = (data[1::3]+392)/6081.8245    
    ICP  = (data[2::3]+5)/84.0552
    return ABP,ECG,ICP

# The following function is used to generate and update the plot widget
# Here we use three series to display three signals
def update_series(j,ABP,ECG,ICP):
    """update_series
    This function is used to update the data in the plot widget
    Here we assign ABP, ECG and ICP to different channels

    Args:
        j: the index of the data
        ABP: the data of ABP
        ECG: the data of ECG
        ICP: the data of ICP

    """
    labels = "Arterial Blood Pressure", "Electrocardiogram", "Intracranial Pressure"
    data = [ABP[j:j+500], ECG[j:j+500], ICP[j:j+500]]
    for tag, label, datay in zip(TAGS, labels, data):
        datax = np.arange(500)/50
        dpg.set_value(tag, [datax, datay])
        dpg.set_item_label(tag, label)

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

        labels = "ABP", "EEG", "ICP"
        y_labels = "amplitude/ mmHg", "amplitude/ mV", "amplitude/ mmHg"
        plot_tags = "y_axis1", "y_axis2", "y_axis3"

        # we use a for loop to create three plot widgets
        for i, (y_label,label, plot_tag) in enumerate(zip(y_labels,labels, plot_tags)):
            with dpg.plot(label=label, height=200, width=600):
                # optionally create legend
                dpg.add_plot_legend()

                # REQUIRED: create x and y axes
                dpg.add_plot_axis(dpg.mvXAxis, label="time")
                dpg.add_plot_axis(dpg.mvYAxis, label=y_label, tag=plot_tag)

                # series belong to a y axis
                # We use the following codes to generate data for initialize plotting
                dpg.add_line_series(np.arange(0,500), np.zeros(500), parent=plot_tag, tag=TAGS[i])

def start_dearpygui(ABP,ECG,ICP):
    """ update the GUI frame by frame
    Here we change dpg.start_dearpygui() to while dpg.is_dearpygui_running() and dpg.render_dearpygui_frame()
    This is because we want to update the plot widget in a loop, if we use dpg.start_dearpygui(), the GUI will
    be frozen and the plot widget will not be updated.

    Args:
        ABP: the data of ABP
        ECG: the data of ECG
        ICP: the data of ICP

    """  
    i = 0
    while dpg.is_dearpygui_running():
        if i >= len(ICP)-500:
            i = 0
        i = i + 1
        update_series(i,ABP,ECG,ICP)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":

    # start the GUI
    dpg.create_context()
    dpg.create_viewport(title='Multiple channel display', width=600, height=700)

    # The following codes are custom functions to create windows
    create_window()
    ABP,ECG,ICP = read_data()

    # The setup_dearpygui() function is used to setup the viewport.
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # As we will manually render the frame, we do not need to use dpg.start_dearpygui(). We used a customized function instead.
    start_dearpygui(ABP,ECG,ICP)
    # All dearpygui apps end with destroy_context()
    dpg.destroy_context()