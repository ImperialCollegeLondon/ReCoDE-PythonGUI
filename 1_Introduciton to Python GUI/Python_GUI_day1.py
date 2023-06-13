# we will be using dearpygui library for GUI
# math is imported to generate data for plotting
import dearpygui.dearpygui as dpg
import math

# All dearpygui apps start with create_context()
dpg.create_context()
# The viewport is the window created by the operating system to display the GUI. 
# The viewport is created using the create_viewport() function
dpg.create_viewport(title='demonstration of dearpygui widgets', width=1000, height=700)

# The following codes generate data for plotting
sindatax = []
sindatay = []
for i in range(0, 500):
    sindatax.append(i / 1000)
    sindatay.append(0.5 + 0.5 * math.sin(50 * i / 1000))

### Start creating GUI ###

"""
In Python, the with statement is used for working with objects that support a context manager protocol. 
It ensures that resources are properly managed and cleaned up when they are no longer needed. Here,
the with statement is used to create a window and all the widgets added to the window will be automatically
added to the window. The same for when you create a menu bar and plot widget.
"""

# We first create a window using the window() function
with dpg.window(label="Window1", width=700, height=700,pos=[0,0]):
    # All the following widgets are added to Window1
    dpg.add_text("Text widget")
    dpg.add_button(label="Button widget")
    dpg.add_input_text(label="Input text widget", default_value="Input text box widgets")
    dpg.add_slider_float(label="Slider widget", default_value=0.273, max_value=1)
    dpg.add_text("Text widget")
    dpg.add_checkbox(label="Checkbox widget - option 1")
    dpg.add_checkbox(label="Checkbox widget - option 2")
    dpg.add_checkbox(label="Checkbox widget - option 3")
    """
    For each widget, parameter pos=[x,y] (x is the horizontal position and y is the vertical position)
    can be used to set the position of the widget. If not set, the widget will be placed automatically.
    In this case, the radio button will be set below the checkbox widgets rather than side by side.
    You can have a try by deleting the pos=[220,140] parameter.
    """
    dpg.add_radio_button(["Radio button widget - option 1", "Radio button widget - option 2", "Radio button widget - option 3"], horizontal=False,pos=[220,140])
   
    # The following codes create a plot widget
    with dpg.plot(label="Line Series", height=300, width=400):
    # optionally create legend
        dpg.add_plot_legend()
        # REQUIRED: create x and y axes
        dpg.add_plot_axis(dpg.mvXAxis, label="x")
        dpg.add_plot_axis(dpg.mvYAxis, label="y", tag="y_axis")
        # series belong to a y axis
        dpg.add_line_series(sindatax, sindatay, label="0.5 + 0.5 * sin(x)", parent="y_axis") 

# There can be as many windows as you want in a viewport, here we generate a second window
with dpg.window(label="Window2", width=700, height=700,pos=[700,0]):
    dpg.add_text("Text widget")

# We define a callback function to print the sender and data of a widget
def print_me(sender, data):
    print(sender, data)
# The following codes create a menu bar
with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save", callback=print_me)
        dpg.add_menu_item(label="Save As", callback=print_me)

        with dpg.menu(label="Settings"):
            dpg.add_menu_item(label="Setting 1", callback=print_me, check=True)
            dpg.add_menu_item(label="Setting 2", callback=print_me)

    dpg.add_menu_item(label="Help", callback=print_me)

    with dpg.menu(label="Widget Items"):
        dpg.add_checkbox(label="Pick Me", callback=print_me)
        dpg.add_button(label="Press Me", callback=print_me)
        dpg.add_color_picker(label="Color Me", callback=print_me)


dpg.setup_dearpygui()
# The viewport is shown using the show_viewport() function.
dpg.show_viewport()
#  The render loop is completely handled by the start_dearpygui() command.
dpg.start_dearpygui()
# All dearpygui apps end with destroy_context()
dpg.destroy_context()