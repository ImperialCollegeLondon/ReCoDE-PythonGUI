import dearpygui.dearpygui as dpg
# numpy is used to read data from file
import numpy as np
# ecgdetectors is used to calculate the heart rate
from ecgdetectors import Detectors

# define the tags for each plot widget
TAGS = "ABP", "ECG", "ICP"

# initialize the start_stop and pause status
start_stop = 0 # 0: stop, 1: start
pause = 0 # 0: unpause, 1: pause

# initialize the filename
filename = "charis4.dat"

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
    with open("Data/"+filename, 'rb') as datafile:
        data = np.fromfile(datafile, np.dtype('int16'))
    ABP  = (data[0::3]+2644)/91.5061
    ECG  = (data[1::3]+392)/6081.8245    
    ICP  = (data[2::3]+5)/84.0552
    return ABP,ECG,ICP

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
    # pause will be used outside the function, so we need to define it as global variable
    global pause

    # if the pause button is pressed, the display will be paused untile unpause button is pressed
    if pause:
        return

    labels = "Arterial Blood Pressure", "Electrocardiogram", "Intracranial Pressure"
    plot_tags = "y_axis1", "y_axis2", "y_axis3"
    data = [ABP[j:j+500], ECG[j:j+500], ICP[j:j+500]]

    # # if the pause button is pressed, the display will be paused untile unpause button is pressed
    # while pause == 1:
    #     dpg.render_dearpygui_frame()

    # update data for each channel
    for tag, label, datay, plot_tag in zip(TAGS, labels, data, plot_tags):
        datax = np.arange(500)/50

        # if the start_stop button is pressed, the display will be stopped and the data will be set to 0
        if start_stop == 0:
            datay = np.zeros(500)

        dpg.set_value(tag, [datax, datay])
        dpg.set_item_label(tag, label)
        dpg.fit_axis_data(plot_tag)
    
    # calculate the heart rate
    if start_stop == 1:
        heart_rate_detector = Detectors(50)
        # using hamilton_detector to detect the R peaks
        r_peaks = heart_rate_detector.hamilton_detector(ECG[j:j+500])
        # calculate the heart rate
        heart_rate = 60/(np.mean(np.diff(r_peaks))/50)
        # update the heart rate
        dpg.set_value("text_heart_rate", str(round(heart_rate,2))+"bpm")

def on_file_dialog_selected(sender, app_data):
    ''' file selection function
    This function is called when a file is selected in the file selection dialog
    The selected file name is used to update the file name in the control window
    and also used to read data from the file.
    
    Args:
        sender: the sender of the callback
        app_data: the data of the selected file
    
    Notes:
        This function is used to update the file name in the control window
    '''

    # update the file name in the control window
    dpg.set_value("text_filename", app_data["file_name"])

    # After the file is selected, the data is read from the file
    # filename, ABP, ECG, ICP will be used outside the function, so we need to define them as global variables
    global filename,ABP,ECG,ICP
    filename = app_data["file_name"]
    ABP,ECG,ICP = read_data()

def on_start_stop_btn_pressed():
    ''' start the display
    Called when START button it clicked, switch the START_STOP between 0 and 1 to start or stop the display
    '''
    # start_stop will be used outside the function, so we need to define it as global variable
    global start_stop

    if start_stop == 0:
        start_stop = 1
        # set the label of the button to STOP
        dpg.set_item_label("START_STOP_BTN", "STOP")
        dpg.enable_item("PAUSE_BTN")
    else:
        start_stop = 0
        # set the label of the button to START
        dpg.set_item_label("START_STOP_BTN", "START")
        dpg.disable_item("PAUSE_BTN")

def on_pause_btn_pressed():
    ''' pause the display
    Called when PAUSE button is clicked, switch the PAUSE between 0 and 1 to pause or unpause the display
    '''
    # pause will be used outside the function, so we need to define it as global variable
    global pause
    
    if pause == 0: #and start_stop == 1: # pause function is only available when the display is started
        pause = 1
        # set the label of the button to UNPAUSE
        dpg.set_item_label("PAUSE_BTN", "UNPAUSE")
        dpg.disable_item("START_STOP_BTN")
    else:
        pause = 0
        # set the label of the button to PAUSE
        dpg.set_item_label("PAUSE_BTN", "PAUSE")
        dpg.enable_item("START_STOP_BTN")

def on_color_set_btn_pressed():
    '''change the color of the plot
    Called when SET button is clicked, change the color of the plot according to the selected channel and color
    '''
    # Using set_value(), we set the value picked from color_picker to the theme color of the selected channel
    '''
    Some tricks are used here. 
    We defined a list named colors_name, which contains the names of the theme colors of the three channels.
    The names of the theme colors are ABP_color, ECG_color and ICP_color. However, from the color_combo, we can only get ABP, ECG and ICP.
    So we need to add ABP, ECG and ICP to the names of the theme colors to get the names of the theme colors of the three channels.
    Taking ABP as an example, we get "ABP" from the color_combo and add "_color" to it. So the varibale name becomes "ABP_color", which
    is the name of the theme color.
    '''
    if dpg.get_value("color_combo") == "ABP":
        dpg.set_value(themes["ABP_theme"], dpg.get_value("color_picker"))
    elif dpg.get_value("color_combo") == "ECG":
        dpg.set_value(themes["ECG_theme"], dpg.get_value("color_picker"))
    elif dpg.get_value("color_combo") == "ICP":
        dpg.set_value(themes["ICP_theme"], dpg.get_value("color_picker"))

def create_display_window():
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
    with dpg.window(label="Display", tag="win"):

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

def create_control_window():
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
    with dpg.window(label="Control", tag="win2",pos=[615,0],width=235,height=700):

        '''
        Pay attention that all the widgets are located by the relative location to the window,
        which is determined by the pos parameter of the item.
        '''

        # The following codes are used to create a text to show the file name
        dpg.add_text("FILENAME:",pos=[10,25])
        dpg.add_text("charis4.dat",tag="text_filename",pos=[80,25])

        # The following codes are used to create a button to select file
        dpg.add_button(label="SELECT FILE",callback=lambda: dpg.show_item("file_selection_dialog"), tag="FILE_BTN", width=140,height=40,pos=[35,50])
        
        # The following codes are used to create START and PAUSE buttons
        dpg.add_button(label="START", callback=on_start_stop_btn_pressed, tag="START_STOP_BTN",width=70,height=40,pos=[30,100])
        dpg.add_button(label="PAUSE", callback=on_pause_btn_pressed, tag="PAUSE_BTN",width=70,height=40, pos=[110,100])
        dpg.disable_item("PAUSE_BTN")

        # The following codes are used to create checkboxes
        # When the checkbox is checked, the corresponding channel will be displayed
        dpg.add_text("Channel selection:",pos=[10,150])
        dpg.add_checkbox(label="Arterial Blood Pressure", pos=[10,175], default_value=True, callback=lambda sender, data: dpg.configure_item("y_axis1", show=data))
        dpg.add_checkbox(label="Electrocardiogram", pos=[10,200], default_value=True, callback=lambda sender, data: dpg.configure_item("y_axis2", show=data))
        dpg.add_checkbox(label="Intracranial Pressure", pos=[10,225],default_value=True, callback=lambda sender, data: dpg.configure_item("y_axis3", show=data))

        # The fowllowing codes are used to create a color picker to change the color of the plot
        dpg.add_text("Color selection:",pos=[10,260])
        dpg.add_color_picker(label="Color", default_value=[255, 0, 0, 255], pos=[10,285], width=200, tag="color_picker")
        dpg.add_text("Set color for:",pos=[10,545])
        dpg.add_combo(items=["ABP", "ECG", "ICP"], default_value="ABP", pos=[110,545], width=50, tag="color_combo")
        dpg.add_button(label="SET", callback=on_color_set_btn_pressed, tag="COLOR_SET_BTN", pos=[170,540], width=30, height=30)
        # To change the color of item in dearpygui, we need to create a theme with specified color and bind the theme to the item
        # Create three themes for three channels
        global themes
        themes = {}
        global tags_theme 
        tags_theme = "ABP_theme", "ECG_theme", "ICP_theme"
        for i,(tag_theme, tag) in enumerate(zip(tags_theme, TAGS)):
            with dpg.theme(tag=tag_theme):
                with dpg.theme_component(dpg.mvLineSeries):
                    themes[tags_theme[i]] = dpg.add_theme_color(dpg.mvPlotCol_Line, (51, 255, 255), category=dpg.mvThemeCat_Plots)
            # bind the theme to the item, when we change the color the the theme, the color of the item will be changed
            dpg.bind_item_theme(tag, tag_theme)

        # The following codes are used to create a text to show the analysis result
        dpg.add_text("Analysis result:",pos=[10,580])
        dpg.add_text("Heart rate:",pos=[10,605])
        # The heart rate will be calculated and updated
        dpg.add_text("60bpm",tag="text_heart_rate",pos=[100,605])

def create_file_selection_dialog():
    """ create a file selection dialog
    This function is used to create a file selection dialog
    This dialog is used to select the data file
    """
    with dpg.file_dialog(directory_selector=False, show=False,callback=on_file_dialog_selected, tag="file_selection_dialog", width=500, height=500):
        dpg.add_file_extension(".dat")

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
        if i >= len(ICP) or start_stop == 0:
            i = 0
        if not pause:
            i = i + 1
        update_series(i,ABP,ECG,ICP)
        dpg.render_dearpygui_frame()
    dpg.destroy_context()

if __name__ == "__main__":

    # start the GUI
    dpg.create_context()
    dpg.create_viewport(title='Multiple channel display', width=850, height=700)

    # The following codes are custom functions to create windows
    create_display_window()
    create_control_window()

    # Here we create a file selection dialog to select the data file
    create_file_selection_dialog()

    ABP,ECG,ICP = read_data()

    # The setup_dearpygui() function is used to setup the viewport.
    dpg.setup_dearpygui()
    dpg.show_viewport()
    # As we will manually render the frame, we do not need to use dpg.start_dearpygui(). We used a customized function instead.
    start_dearpygui(ABP,ECG,ICP)

    # All dearpygui apps end with destroy_context()
    dpg.destroy_context()