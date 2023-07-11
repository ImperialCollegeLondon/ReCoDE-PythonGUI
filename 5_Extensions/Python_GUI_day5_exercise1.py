import dearpygui.dearpygui as dpg
# numpy and math are used to generate data for the plot widget
import numpy as np
# import serial
import serial

SERIAL_TAG = "series_tag"
# initialize the start_stop status
start_stop = 0 # 0: stop, 1: start
# initialize the data array
# For illustration purpose, we only use 20 points to plot the data
datay = np.zeros(20)
# create a serial object
ser = serial.Serial('COM1', 9600, timeout=0.1)

# The following codes are used to update the plot widget
# It is the same as the codes in previous example. The only difference is that we replace the random data with ICP data.
def update_series():
    """update data for plotting
    This function is used to update data from files for plotting.
    when you display data dynamically, you need to specify the length of the data
    in this case, the length of the data is 500, that is, there are 500 points in the plot widget
    
    Args:
        j: the index of the data
        ICP: the data of ICP
    """
    datax = np.arange(20)

    # read data from the serial port
    received_data = 0
    if not(start_stop == 1 and ser.in_waiting):
        return
    
    received_data = ser.readline().decode('utf-8').strip('\r\n').split('\r')
    # Only one point is sent from the serial port each time, so we need to concatenate the data
    # datay is initialized as a zero array with length 500, the recieved data is added to the end of the array
    # we then contruncate the first element of the array, so the length of the array is still 500
    global datay

    # The following codes are used to deal with multiple data points sent from the serial port
    received_data_display = []
    for i in range(len(received_data)):
        received_data_display.append(received_data[i].split(' '))
    received_data_display = np.array(received_data_display)
    received_data_display.reshape(1,np.size(received_data_display))
    datay = np.append(datay, received_data_display[0].astype(np.float64))
    datay = np.delete(datay, np.arange(0,len(received_data_display[0])))

    if start_stop == 0:
        datay = np.zeros(20)

    dpg.set_value(SERIAL_TAG, [datax, datay])
    dpg.set_item_label(SERIAL_TAG,'Serial Transmission')
    dpg.fit_axis_data("y_axis")

def on_start_stop_pressed():
    """start or stop the plot
    This function is used to start or stop the plot
    """
    global start_stop
    if start_stop == 0:
        start_stop = 1
        dpg.configure_item("START_STOP_BTN", label="STOP")
        if not ser.is_open:
            ser.open()
    else:
        start_stop = 0
        dpg.configure_item("START_STOP_BTN", label="START")
        ser.close()

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
        with dpg.plot(label="Serial Transmittion", height=300, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="time/s", tag="x_axis")
            dpg.add_plot_axis(dpg.mvYAxis, label="y/mmHg", tag="y_axis")

            # series belong to a y axis
            dpg.add_line_series(np.arange(0,20), np.zeros(20), parent="y_axis", tag=SERIAL_TAG)
        
        # create a START/STOP button
        dpg.add_button(label="START", callback=on_start_stop_pressed, tag="START_STOP_BTN")

    
def start_dearpygui():
    """ update the GUI frame by frame
    Here we change dpg.start_dearpygui() to while dpg.is_dearpygui_running() and dpg.render_dearpygui_frame()
    This is because we want to update the plot widget in a loop, if we use dpg.start_dearpygui(), the GUI will
    be frozen and the plot widget will not be updated.

    Args:
        ICP: the data of ICP

    """    
    while dpg.is_dearpygui_running():
        update_series()
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":

    # The following codes start the GUI
    dpg.create_context()
    dpg.create_viewport(title='Single channel display', width=600, height=400)

    # The following codes are custom functions to create windows and read data from files
    create_window()

    # The setup_dearpygui() function is used to setup the viewport.
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # As we will manually render the frame, we do not need to use dpg.start_dearpygui(). We used a customized function instead.
    start_dearpygui()
    # All dearpygui apps end with destroy_context()
    dpg.destroy_context()