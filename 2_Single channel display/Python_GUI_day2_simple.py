import dearpygui.dearpygui as dpg
# numpy is used to generate data for the plot widget
import numpy as np

SERIAL_TAG = "series_tag"

# The following function is used to generate and update the plot widget
def update_series(j):
    """update data for plotting
    This function is used to update demo data for plotting.
    The data is generated using the following equation:
    y = 0.5 + 0.5 * sin(50 * x)
    when you display data dynamically, you need to specify the length of the data
    in this case, the length of the data is 500, that is, there are 500 points in the plot widget

    Args:
        j: the index of the data

    """
    cosdatax = np.arange(500)/1000
    cosdatay = 0.5 + 0.5 * np.cos(50 * (cosdatax+j/ 1000))
    """
    Pay attention
    When you plot data with GUI, you need to use dpg.set_value() to update the data, the data will be shown
    in the plot widget with the tag "series_tag", this tag is assigned to the plot widget at line 46.
    """
    dpg.set_value(SERIAL_TAG, [cosdatax, cosdatay])
    dpg.set_item_label(SERIAL_TAG, "0.5 + 0.5 * cos(x)")

# The following function is used to start the GUI
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
        with dpg.plot(label="Line Series", height=300, width=600):
            # optionally create legend
            dpg.add_plot_legend()

            # REQUIRED: create x and y axes
            dpg.add_plot_axis(dpg.mvXAxis, label="x")
            dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")

            # series belong to a y axis
            # We use the following codes to generate data for initialize plotting
            dpg.add_line_series(np.arange(500/1000), np.zeros(500), parent="y_axis", tag=SERIAL_TAG)

def start_dearpygui():
    """ update the GUI frame by frame
    Here we change dpg.start_dearpygui() to while dpg.is_dearpygui_running() and dpg.render_dearpygui_frame()
    This is because we want to update the plot widget in a loop, if we use dpg.start_dearpygui(), the GUI will
    be frozen and the plot widget will not be updated.
    """
    i = 0
    while dpg.is_dearpygui_running():
        i = i + 1
        update_series(i)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":
    
    dpg.create_context()
    dpg.create_viewport(title='Single channel display', width=600, height=400)

    # The following codes are custom functions to create windows
    create_window()

    # The setup_dearpygui() function is used to setup the viewport.
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # As we will manually render the frame, we do not need to use dpg.start_dearpygui(). We used a customized function instead.
    start_dearpygui()
    # All dearpygui apps end with destroy_context()
    dpg.destroy_context()