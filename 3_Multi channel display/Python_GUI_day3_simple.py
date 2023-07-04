import dearpygui.dearpygui as dpg
# math is used to generate data for the plot widget
import numpy as np

# define the tags for each plot widget
TAGS = "series_tag1", "series_tag2", "series_tag3"

def update_series(j):
    """update_series
    This function is used to update the data in the plot widget
    Here we generate separate data for each plot widget

    Args:
        j: the index of the data

    """
    funs = np.cos, np.sin, np.tan
    labels = "0.5 + 0.5 * cos(x)", "0.5 + 0.5 * sin(x)", "0.5 + 0.5 * tan(x)"

    # we use a for loop to update the data for each plot widget
    for tag, fun, label in zip(TAGS, funs, labels):
        datax = np.arange(500)/1000
        datay = fun(50 * (datax+j/ 1000))
        dpg.set_value(tag, [list(datax), list(datay)])
        dpg.set_item_label(tag, label)

def create_window():
    """ docstring for create_window
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

        label = "Line Series1", "Line Series2", "Line Series3"
        plot_tags = "y_axis1", "y_axis2", "y_axis3"

        # we use a for loop to create three plot widgets
        for i, (label, plot_tag) in enumerate(zip(label, plot_tags)):
            with dpg.plot(label=label, height=200, width=600):
                # optionally create legend
                dpg.add_plot_legend()

                # REQUIRED: create x and y axes
                dpg.add_plot_axis(dpg.mvXAxis, label="x")
                dpg.add_plot_axis(dpg.mvYAxis, label="y", tag=plot_tag)

                # series belong to a y axis
                # We use the following codes to generate data for initialize plotting
                dpg.add_line_series(np.arange(500/1000), np.zeros(500), parent=plot_tag, tag=TAGS[i])

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

    # start the GUI
    dpg.create_context()
    dpg.create_viewport(title='Multiple channel display', width=600, height=700)

    # The following codes are custom functions to create windows
    create_window()

    # The setup_dearpygui() function is used to setup the viewport.
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # As we will manually render the frame, we do not need to use dpg.start_dearpygui(). We used a customized function instead.
    start_dearpygui()
    # All dearpygui apps end with destroy_context()
    dpg.destroy_context()